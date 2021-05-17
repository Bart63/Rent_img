from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from GUI import GUI

class Client_Screen(GridLayout):
    pass

class Client(GUI):
    __balance__ = 0

    def __init__(self):
        super(Client, self).__init__()

    def build(self):
        return Client_Screen()

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