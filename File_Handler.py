import os
class File_Handler:
    def Exist(self) -> bool:
        pass

    def Read(self,file ,n = -1):
        f = open(file,'r')
        if n >= 0 and n >= f:
            for line in f:
                f.readline()
                if line == n:
                    return f.readline()
        else:
            file_lines = [line.strip("\n") for line in f if line != "\n"]
            return file_lines
        f.close()

    def Update(self,file,st,n = -1):
        f = open(file,'w')
        if n >= 0 and n >= f:
            for line in f :
                f.readline()
                if line == n:
                    f.write(st)


    def Write(self, st,file):
        f = open(file,'a')
        f.write(file,st)
        f.close()

    def Clear(self,file):
        os.remove(file)
        f = open(file,'x')
        f.close()