from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from GUI import GUI

class Creator(GUI):
    def __init__(self):
        super(Creator, self).__init__()

    def build(self):
        gr = GridLayout(
            rows=5,
            cols=2
        )
        gr.add_widget(Label(text="Nazwa:"))
        gr.add_widget(TextInput(multiline=False))
        gr.add_widget(Label(text="Opis:"))
        gr.add_widget(TextInput(multiline=False))
        gr.add_widget(Label(text="Cena:"))
        gr.add_widget(TextInput(multiline=False))
        gr.add_widget(Label(text="Zdjęcie:"))
        gr.add_widget(Button(text="Wybierz zdjęcie"))
        gr.add_widget(Label())
        gr.add_widget(Button(text="Wyślij"))
        return gr

    def Send(self):
        pass

if __name__=='__main__':
    Creator().run()