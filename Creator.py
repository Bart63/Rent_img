from kivy.uix.gridlayout import GridLayout
from GUI import GUI

class Creator_Screen(GridLayout):
    pass

class Creator(GUI):
    def __init__(self):
        super(Creator, self).__init__()

    def build(self):
        return Creator_Screen()

if __name__=='__main__':
    Creator().run()