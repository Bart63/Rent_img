from kivy.app import App
from kivy.core.image import Image as CoreImage, Texture
from kivy.uix.image import Image

class TestApp(App):
    def build(self):
        ci = CoreImage("usmiech2.png")
        img = Image()
        img.texture = ci.texture
        return img

if __name__=='__main__':
    TestApp().run()