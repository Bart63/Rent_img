from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from GUI import GUI

class Client(GUI):
    __balance__ = 0

    def __init__(self):
        super(Client, self).__init__()

    def build(self):
        gr = GridLayout(
            rows=5,
            cols=2
        )
        gr.add_widget(Label(text="Wypożyczone:"))
        gr.add_widget(TextInput(multiline=False))
        gr.add_widget(Label(text="Do wypożyczenia:"))
        gr.add_widget(TextInput(multiline=False))
        return gr

    def SetBalance(self):
        pass

    def Search(self):
        pass

    def Lend(self):
        pass

    def Show(self):
        pass

    def Open(self):
        pass

if __name__=='__main__':
    Client().run()