from os import remove
from linecache import getline

path = "program_data.txt"

class File_Handler:
    def Read(self, filename=path, n=-1):
        res = ""
        if n==-1:
            f = open(filename, 'r')
            res = f.readlines()
            f.close()
        else:
            res = getline(filename, n)
        return res

    def NumberOfLines(self, filename=path):
        f = open(filename)
        num = sum(1 for _ in f)
        f.close()
        return num

    def Update(self, st, filename=path, n=-1):
        f = open(filename, 'w')
        if n>=0 and n<self.NumberOfLines(filename):
            for line in f:
                f.readline()
                if line == n:
                    f.write(st)
        f.close()

    def Write(self, st, filename=path):
        f = open(filename, 'a')
        f.write(st+'\n')
        f.close()

    def Clear(self, filename=path):
        remove(filename)
        f = open(filename, 'x')
        f.close()