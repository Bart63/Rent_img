class ImageRaw:
    def __init__(self, path) -> None:
        self.img = open(path, 'rb')

    def Get_Img(self):
        return self.img