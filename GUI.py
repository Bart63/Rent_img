from kivy.app import App
from kivy.properties import ObjectProperty
from kivy.uix.textinput import TextInput
from kivy.uix.popup import Popup
from Manager import Manager
import re

class Login_Popup(Popup):
    username, password = ObjectProperty(None), ObjectProperty(None)
    def login(self):
        data = {
            "username": self.username.text,
            "password": self.password.text
        }
        status = GUI.Log_in(data)
        if status:
            self.dismiss()

class LoginInput(TextInput):
    patt = re.compile("[^a-zA-Z0-9]")
    def insert_text(self, substring, from_undo=False):
        substring = "".join(re.split(self.patt, substring))
        return super().insert_text(substring, from_undo=from_undo)

class PasswordInput(TextInput):
    def insert_text(self, substring, from_undo=False):
        substring = "".join(substring.split())
        return super().insert_text(substring, from_undo=from_undo)

class GUI(App):
    def __init__(self):
        super(GUI, self).__init__()
    
    def on_start(self):
        self.Show_Popup()

    def Get_Manager(self):
        return Manager()

    def Log_in(data):
        return Manager().Log_in(data)

    def Show_Popup(self):
        popupWindow = Login_Popup()
        popupWindow.open()