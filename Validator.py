import os.path

extentions = ['.png', '.jpg', '.jpeg']

class Validator:
    def IsValidString(self, text, max_length) -> bool:
        return type(text)==str and len(text)<=max_length and len(text)>0

    def IsValidInt(self, value, max_val) -> bool:
        return type(value)==int and value<=max_val and value>0

    def IsValidPath(self, path) -> bool:
        if os.path.isfile(path):
            name,extention = os.path.splitext(path)
            for ext in extentions:
                if extention == ext:
                    return True
        return False