import os.path

class Validator:
    def IsString(self):
        pass

    def IsQuery(self) -> bool:
        pass

    def IsBalance(self) -> bool:
        pass

    def IsValidString(self,text,max_length) -> bool:
        if (type(text)==str and len(text)<=max_length and len(text) > 0):
            return True
        else:
            return False

    def IsValidInt(self,value,max_val) -> bool:
            if(type(value)==int and value<=max_val and value>0 ):
                return True
            else:
                return False

    def IsValidPath(self,path,):

