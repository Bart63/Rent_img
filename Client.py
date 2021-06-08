from kivy.app import App
from kivy.core.text import Label
from Manager import Manager
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.properties import ObjectProperty
from GUI import GUI
from kivy.core.image import Image as CoreImage
from kivy.uix.image import Image

class Client_Screen(GridLayout):
    balance = ObjectProperty(None)
    def Show_Shop(self):
        Shop_Popup().open(self)

    def Show_Rented(self):
        Rented_Popup().open()
    
    def Add_Balance(self, val=10):
        Client.__balance__ += val
        self.balance.text = f"Balans: {Client.__balance__}$"

    def Random_Image(self):
        res = Client().Random_Image()
        if not res:
            return
        id = res['id_obrazu']
        responses = Client().Search_Images()
        image = responses[str(id)]
        if Client.__balance__-image['price']>=0:
            Client().Get_Manager().Lend_Imgs(image)
            self.Add_Balance(-image['price'])

class Shop_Popup(Popup):
    def __init__(self, **kwargs):
        kwargs['title'] = 'Sklep'
        super().__init__(**kwargs)

    def save_image(self, *largs):
        id = largs[0].text
        responses = Client().Search_Images()
        image = responses[id]
        if Client.__balance__-image['price']>=0:
            Client().Get_Manager().Lend_Imgs(image)
            self.root.Add_Balance(-image['price'])
        self.dismiss()

    def open(self, *largs, **kwargs):
        self.root = largs[0]
        return super().open(*largs, **kwargs)

    def on_open(self):
        layout = GridLayout(cols=2, spacing=10, size_hint_y=None)
        layout.bind(minimum_height=layout.setter('height'))
        responses = Client().Search_Images()
        for key in responses:
            btn = Button(text=str(responses[key]['id']), size_hint_y=None, height=90, on_press=self.save_image)
            layout.add_widget(btn)
            btn = Button(text=responses[key]['description'], size_hint_y=None, height=90, disabled = True)
            layout.add_widget(btn)
        root = ScrollView(size_hint=(1, None), size=(Window.width, Window.height))
        root.add_widget(layout)
        self.add_widget(root)
        return super().on_open()

class Image_Popup(Popup):
    def __init__(self, img, title, **kwargs):
        kwargs['title'] = str(title)
        self.img = img
        super().__init__(**kwargs)

    def on_open(self):
        self.add_widget(self.img)
        return super().on_open()

class Rented_Popup(Popup):
    def __init__(self, **kwargs):
        kwargs['title'] = 'Wypożyczone'
        super().__init__(**kwargs)

    def open_image(self, *largs):
        id = int(largs[0].text)
        responses = Client().Show_Images(id)
        image = responses[0]
        decoded_img = Client().Open_Image(image['images'])
        ci = CoreImage(decoded_img, ext='png')
        img = Image()
        img.texture = ci.texture
        Image_Popup(img, image['description']).open()
        self.dismiss()
        
    def on_open(self):
        layout = GridLayout(cols=2, spacing=10, size_hint_y=None)
        layout.bind(minimum_height=layout.setter('height'))
        images = Client().Show_Images()
        for img in images:
            btn = Button(text=str(img['id']), size_hint_y=None, height=90, on_press=self.open_image)
            layout.add_widget(btn)
            btn = Button(text=img['description'], size_hint_y=None, height=90, disabled = True)
            layout.add_widget(btn)
        root = ScrollView(size_hint=(1, None), size=(Window.width, Window.height))
        root.add_widget(layout)
        self.add_widget(root)
        return super().on_open()

class Client(GUI):
    __balance__ = 0
    def __init__(self):
        super(Client, self).__init__()

    def Search_Images(self):
        return Manager().Search_Imgs()

    def Show_Images(self, num=-1):
        return Manager().Show_Imgs(num)
    
    def Open_Image(self, img):
        return Manager().Open_Imgs(img)

    def Random_Image(self):
        return Manager().Ranom_Img()

    def build(self):
        return Client_Screen()

if __name__=='__main__':
    Client().run()

def run():
    Client().run()