# 1번

from PIL import Image

try:
    i1 = Image.open("c1.jpg")
    i2 = Image.open("c2.jpg")
except IOError as err:
    print("unable to load image")

box = (0,0,550,343)
i1c = i1.crop(box)      # 두 사진의 크기가 맞지 않아 자름.

im_blend = Image.blend(i1c,i2,0.3)

im_blend.show()

# 2번
from tkinter import *

s = input("문자열을 입력하시오:")
result = ''
for i in s:
    if i.islower():
        result += i
root = Tk()
l = Label(root,text='')
l.pack

b = Button(root,text='result')
b.pack()

root.mainloop()
