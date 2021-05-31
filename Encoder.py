import base64

class Encoder:
    def encode(self, path):
        img = open(path, 'rb')
        encoded_img = base64.b64encode(img.read())
        return encoded_img.decode('utf-8')