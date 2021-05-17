from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.popup import Popup
from kivy.properties import ObjectProperty
from GUI import GUI
import os

class Creator_Screen(GridLayout):
    name = ObjectProperty(None)
    desc = ObjectProperty(None)
    price = ObjectProperty(None)
    path = ObjectProperty(None)

    def dismiss_popup(self):
        self._popup.dismiss()

    def show_load(self):
        content = LoadDialog(load=self.load, cancel=self.dismiss_popup)
        self._popup = Popup(title="Wybierz plik", content=content,
                            size_hint=(0.9, 0.9))
        self._popup.open()

    def load(self, path, filename):
        self.path.text = os.path.join(path, filename[0])
        self.dismiss_popup()

    def send_photo(self):
        print({
            "name": self.name.text,
            "desc": self.desc.text,
            "price": self.price.text,
            "path": self.path.text
        })

class LoadDialog(FloatLayout):
    load = ObjectProperty(None)
    cancel = ObjectProperty(None)

class Creator(GUI):
    def __init__(self):
        super(Creator, self).__init__()

    def build(self):
        return Creator_Screen()

if __name__=='__main__':
    Creator().run()