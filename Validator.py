import os.path

class Validator:
    def IsString(self):
        pass

    def IsQuery(self) -> bool:
        pass

    def IsBalance(self) -> bool:
        pass

    def IsValidString(self,text,max_length) -> bool:
        return (type(text)==str and 0<len(text)<=max_length)

    def IsValidInt(self,value,max_val) -> bool:
        return type(value)==int and 0<value<=max_val

    def IsValidPath(self,path):
        pass