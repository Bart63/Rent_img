from Validator import Validator
from File_Handler import File_Handler
from ImageCodedAdapter import ImageCodedAdapter
from ImageRawAdapter import ImageRawAdapter
from requests import get, post
from datetime import datetime, timedelta

class Manager:
    def __init__(self):
        self.validator = Validator()
        self.f_handler = File_Handler()
        
    def Log_in(self, data) -> bool: 
        if not Validator().IsValidAllLogin(data):
            return False
        r = post('http://127.0.0.1:5000/login', json=data)
        if r.status_code==200 or r.status_code==409:
            return True
        return False
    
    def Ranom_Img(self) -> dict:
        data = {'login': 'login', 'czas_zakonczenia': 'czas_zakonczenia'}
        r = post('http://127.0.0.1:5000/rent_image/random', json=data)
        if r.status_code==200 or r.status_code==409:
            return r.json()
        return {}

    def Search_Imgs(self):
        r = get('http://127.0.0.1:5000/images')
        return r.json()

    def Lend_Imgs(self, data):
        self.f_handler.Write(str(data['id']))
        self.f_handler.Write(data['description'])
        self.f_handler.Write(data['images'])
        delta_time = timedelta(days=1)
        current_date = datetime.now()
        expiration_date = current_date+delta_time
        self.f_handler.Write(expiration_date.isoformat())

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
        lines = self.f_handler.Read()
        for ind,el in enumerate(lines):
            lines[ind] = el.replace("\n", "")
        self.RemoveExpired(lines)
        lines = self.f_handler.Read()
        for ind,el in enumerate(lines):
            lines[ind] = el.replace("\n", "")
        imgs = []
        for i in range(0, len(lines), 4):
            imgs.append({
                'id' : int(lines[i]),
                'description' : lines[i+1],
                'images' : lines[i+2]
            })
        if num==-1:
            return imgs
        else:
            return [img for img in imgs if img['id']==num]

    def Open_Imgs(self, img):
        img_coded = ImageCodedAdapter(img)
        return img_coded.Get_Img()

    def RemoveExpired(self, lines):
        current_date = datetime.now()
        not_expired = []
        for i in range(0, len(lines), 4):
            expiration_date = datetime.fromisoformat(lines[i+3])
            if current_date<expiration_date:
                not_expired.extend(lines[i:i+4])
        self.f_handler.Clear()
        for st in not_expired:
            self.f_handler.Write(st)