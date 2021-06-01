from ImageRaw import ImageRaw
from ImageCoded import ImageCoded
from io import BytesIO
from base64 import b64decode

class ImageCodedAdapter(ImageCoded, ImageRaw):
    def __init__(self, decoded_img) -> None:
        super(ImageCodedAdapter, self).__init__(decoded_img)
        self.img = self.Decode()

    def Decode(self):
        ready_to_decode = self.decoded_img.encode('utf-8')
        decoded_img = BytesIO(b64decode(ready_to_decode))
        return decoded_img