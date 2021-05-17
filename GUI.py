from kivy.app import App
from kivy.properties import ObjectProperty
from kivy.uix.textinput import TextInput
from kivy.uix.popup import Popup
from Manager import Manager
import re

class Login_Popup(Popup):
    name, password = ObjectProperty(None), ObjectProperty(None)
    def login(self):
        print({
            "name": self.name.text,
            "password": self.password.text
        })
        self.dismiss()

class LoginInput(TextInput):
    patt = re.compile("[^a-zA-Z0-9]")
    def insert_text(self, substring, from_undo):
        substring = "".join(re.split(self.patt, substring))
        return super().insert_text(substring, from_undo=from_undo)

class PasswordInput(TextInput):
    def insert_text(self, substring, from_undo):
        substring = "".join(substring.split())
        return super().insert_text(substring, from_undo=from_undo)

class GUI(App):
    def __init__(self):
        super(GUI, self).__init__()
        self.manager = Manager()
    
    def on_start(self):
        self.Show_Popup()

    def Show_Popup(self):
        popupWindow = Login_Popup()
        popupWindow.open()