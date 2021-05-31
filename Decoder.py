from PIL import Image
from io import BytesIO
import base64

class Decoder:
    def decode(self, decoded_img):
        ready_to_decode = decoded_img.encode('utf-8')
        decoded_img = BytesIO(base64.b64decode(ready_to_decode))
        return decoded_img