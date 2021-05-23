import os
class File_Handler:
    def Exist(self) -> bool:
        pass

    def Read(self,file ,n = -1):
        f = open(file,'r')
        if n >= 0 and n >= f:
            for line in f:
                if line == n:
                    return line
        else:
            file_lines = [line.strip("\n") for line in f if line != "\n"]
            return file_lines
        f.close()



    def Write(self, st,file):
        f = open(file,'a')
        f.write(file,st)
        f.close()

    def Clear(self,file):
        os.remove(file)
        f = open(file,'x')
        f.close()