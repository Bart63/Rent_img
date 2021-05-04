from kivy.app import App
from Manager import Manager

class GUI(App):
    def __init__(self):
        super(GUI, self).__init__()
        self.manager = Manager()
    
    def Close(self):
        pass

    def Click(self):
        pass