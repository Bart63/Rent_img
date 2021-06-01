from Client import run as ClientRun
from Creator import run as CreatorRun
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.app import App

class GUIChooser(App):
    def __init__(self):
        super(GUIChooser, self).__init__()
    
    def build(self):
        layout = GridLayout(cols=2, rows=1)
        btn = Button(text="Klient", on_press=self.RunClient)
        layout.add_widget(btn)
        btn = Button(text="Twórca", on_press=self.RunCreator)
        layout.add_widget(btn)
        return layout

    def RunClient(self, *args):
        self.stop()
        ClientRun()

    def RunCreator(self, *args):
        self.stop()
        CreatorRun()

if __name__=='__main__':
    GUIChooser().run()