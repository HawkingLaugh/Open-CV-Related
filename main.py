import cv2
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
    return filelist

def face_dection(i):
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    img = cv2.imread(i)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # face_cascade.detectMultiScale(image,scaleFactor=1.08,minNeighbors=5,minSize=(32, 32))
    # faces returns how many faces found. if faces > 0 == found 
    faces = face_cascade.detectMultiScale(gray,scaleFactor=1.08,minNeighbors=5,minSize=(128, 128))

    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y), (x+w, y+h), (0,255,0), 2)

    if len(faces) > 0:
        cv2.imwrite('{}_result.jpg'.format(i),img)

if __name__ == "__main__":
    files = fList()
    for i in files:
        face_dection(i)