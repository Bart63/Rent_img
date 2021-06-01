from ImageRaw import ImageRaw
from ImageCoded import ImageCoded
from base64 import b64encode

class ImageRawAdapter(ImageRaw, ImageCoded):
    def __init__(self, path) -> None:
        super(ImageRawAdapter, self).__init__(path)
        self.decoded_img = self.Encode()

    def Encode(self):
        encoded_img = b64encode(self.img.read())
        return encoded_img.decode('utf-8')