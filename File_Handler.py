from os import remove
from linecache import getline

class File_Handler:
    def Read(self, filename, n=-1):
        res = ""
        if n==-1:
            f = open(filename, 'r')
            res = f.readlines()
            f.close()
        else:
            res = getline(filename, n)
        return res

    def Update(self, filename, st ,n=-1):
        f = open(filename, 'w')
        if n>=0 and n<sum(1 for _ in f):
            for line in f:
                f.readline()
                if line == n:
                    f.write(st)

    def Write(self, st, filename):
        f = open(filename, 'a')
        f.write(st+'\n')
        f.close()

    def Clear(self, filename):
        remove(filename)
        f = open(filename, 'x')
        f.close()