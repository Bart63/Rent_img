from Validator import Validator
from File_Handler import File_Handler
from Encoder import Encoder
from Decoder import Decoder
import requests
from DictJSONAdapt import DictJSONAdapt

class Manager:
    def __init__(self):
        self.validator = Validator()
        self.f_handler = File_Handler()
        
    def Log_in(self, data) -> bool: 
        if not Validator().IsValidAllLogin(data):
            return False
        data = DictJSONAdapt(data).getJSON()
        r = requests.post('http://127.0.0.1:5000/login', json=data)
        if r.status_code==200:
            return True
        return False
    
    def Search_Imgs(self):
        r = requests.get('http://127.0.0.1:5000/images')
        return r.json()

    def Lend_Imgs(self, data):
        File_Handler().Write(str(data['id']))
        File_Handler().Write(data['description'])
        File_Handler().Write(data['images'])

    def Send_Imgs(self, data):
        if not Validator().IsValidAllSend(data):
            return False
        en_img_json = Encoder().encode(data['path'])
        del data['path']
        data['image'] = en_img_json
        r = requests.post('http://127.0.0.1:5000/images', json=data)
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
        return Decoder().decode(img)

    def Save(self):
        pass

    def Load(self):
        pass

    def RemoveExpired(self):
        pass

if __name__=='__main__':
    Manager().Log_in({
    'username' : 'Bart',
    'password' : 'Bart'
})