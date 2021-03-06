from os import name
from os.path import splitext, isfile
from sys import maxsize

extentions = ['.png', '.jpg', '.jpeg']

class Validator:
    def IsValidAllSend(self, data) -> bool:
        path_valid = self.IsValidPath(data['path'])
        name_valid = self.IsValidString(data['name'])
        desc_valid = self.IsValidString(data['description'])
        price_valid = self.IsValidInt(data['price'])
        return path_valid and name_valid and desc_valid and price_valid

    def IsValidAllLogin(self, data) -> bool:
        name_valid = self.IsValidString(data['username'])
        pass_valid = self.IsValidString(data['password'])
        return name_valid and pass_valid

    def IsValidString(self, text, max_length=maxsize) -> bool:
        return type(text)==str and len(text)<=max_length and len(text)>0

    def IsValidInt(self, value, max_val=maxsize) -> bool:
        return type(value)==int and value<=max_val and value>0

    def IsValidPath(self, path) -> bool:
        if isfile(path):
            name,extention = splitext(path)
            for ext in extentions:
                if extention == ext:
                    return True
        return False