import os
import pathlib
from os import listdir
from os.path import isfile, join

def fList():
    p = pathlib.Path().absolute()
    fin = open('files.txt', 'w+')
    filelist = []
    for f in listdir(path=p):
        if isfile(join(p,f)):
            if '.jpg' in f:
                filelist.append(f)
    for i in filelist:
        fin.write(i)
        fin.write('\n')
    return 