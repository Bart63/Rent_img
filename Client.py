from configparser import NoOptionError
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.properties import ObjectProperty
from kivy.core.window import Window
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from GUI import GUI

class Client_Screen(GridLayout):
    def Show_Items(self):
        Items_Popup().open()

class Items_Popup(Popup):
    def __init__(self, **kwargs):
        kwargs['title'] = 'Items'
        super().__init__(**kwargs)

    def on_open(self):
        layout = GridLayout(cols=1, spacing=10, size_hint_y=None)
        layout.bind(minimum_height=layout.setter('height'))
        for i in range(10):
            btn = Button(text=str(i), size_hint_y=None, height=90, on_press=self.dismiss)
            layout.add_widget(btn)
        root = ScrollView(size_hint=(1, None), size=(Window.width, Window.height))
        root.add_widget(layout)
        self.add_widget(root)
        return super().on_open()

class Client(GUI):
    __balance__ = 0

    def __init__(self):
        super(Client, self).__init__()

    def build(self):
        return Client_Screen()

if __name__=='__main__':
    Client().run()