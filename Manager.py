from Validator import Validator
from File_Handler import File_Handler
from ImageCodedAdapter import ImageCodedAdapter
from ImageRawAdapter import ImageRawAdapter
from requests import get, post

class Manager:
    def __init__(self):
        self.validator = Validator()
        self.f_handler = File_Handler()
        
    def Log_in(self, data) -> bool: 
        if not Validator().IsValidAllLogin(data):
            return False
        r = post('http://127.0.0.1:5000/login', json=data)
        if r.status_code==200:
            return True
        return False
    
    def Search_Imgs(self):
        r = get('http://127.0.0.1:5000/images')
        return r.json()

    def Lend_Imgs(self, data):
        File_Handler().Write(str(data['id']))
        File_Handler().Write(data['description'])
        File_Handler().Write(data['images'])

    def Send_Imgs(self, data):
        if not Validator().IsValidAllSend(data):
            return False
        img_raw = ImageRawAdapter(data['path'])
        en_img_json = img_raw.Get_Coded()
        del data['path']
        data['image'] = en_img_json
        r = post('http://127.0.0.1:5000/images', json=data)
        if r.status_code==200:
            return r.json()['id']
        return False

    def Show_Imgs(self, num=-1):
        lines = File_Handler().Read()
        imgs = []
        for i in range(0, len(lines), 3):
            imgs.append({
                'id' : int(lines[i].replace("\n", "")),
                'description' : lines[i+1].replace("\n", ""),
                'images' : lines[i+2].replace("\n", "")
            })
        if num==-1:
            return imgs
        else:
            return [img for img in imgs if img['id']==num]

    def Open_Imgs(self, img):
        img_coded = ImageCodedAdapter(img)
        return img_coded.Get_Img()

    def RemoveExpired(self):
        pass