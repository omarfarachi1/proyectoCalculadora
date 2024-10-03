from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

class VentanaCalculadora(BoxLayout):
    def __init__(self, **kwargs):
        super(VentanaCalculadora, self).__init__(**kwargs)
        self.orientation = 'vertical'

        self.display = Label(text='', size_hint=(1, 0.2), font_size=30)
        self.add_widget(self.display)
        self.boton_layout = BoxLayout(orientation='vertical', size_hint=(1, 0.8))
        self.add_widget(self.boton_layout)

        self.botones = [
            ['1', '2', '3', '/'],
            ['4', '5', '6', '*'],
            ['7', '8', '9', '-'],
            ['0', '.', '+']
            ]

        for i in self.botones:
            fila = BoxLayout(orientation='horizontal', size_hint=(1, 0.2))
            self.boton_layout.add_widget(fila)
            for texto in i:
                boton = Button(text=texto, font_size=20)
                boton.bind(on_press=self.boton_click)
                fila.add_widget(boton)

        boton_igual = Button(text='=', size_hint=(1, 0.2))
        boton_igual.bind(on_press=self.boton_click)
        self.boton_layout.add_widget(boton_igual)

        boton_limpiar = Button(text='Limpiar', size_hint=(1, 0.2))
        boton_limpiar.bind(on_press=self.boton_click)
        self.boton_layout.add_widget(boton_limpiar)

        boton_borrar = Button(text='Borrar', size_hint=(1, 0.2))
        boton_borrar.bind(on_press=self.boton_click)
        self.boton_layout.add_widget(boton_borrar)

    def boton_click(self, boton):
        if boton.text.isdigit() or boton.text == '.':
            self.display.text += boton.text
        elif boton.text in ['+', '-', '*', '/']:
            self.display.text += ' ' + boton.text + ' '
        elif boton.text == '=':
            try:
                resultado = eval(self.display.text)
                self.display.text = str(resultado)
            except SyntaxError:
                self.display.text = "Expresion invalida"
            except ZeroDivisionError:
                self.display.text = "No se puede dividir por cero"
            except Exception as e:
                self.display.text = "Error: " + str(e)
        elif boton.text == "Limpiar":
            self.display.text = ''

        elif boton.text == 'Borrar':
            if self.display.text:
                self.display.text = self.display.text[:-1]

class Calculadora(App):
    def build(self):
        return VentanaCalculadora()


    def on_start(self):
        self.root_window.size = (300, 400)
        self.root_window.resizable = False


if __name__ == '__main__':
  window = Calculadora()
  window.run()