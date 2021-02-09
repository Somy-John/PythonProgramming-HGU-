from tkinter import *
from functools import partial

def check(rst,str):
    s = str.get()
    s1 = s.strip(' ')
    lst = []
    for i in s1:
        if i.isupper():
            i = i.lower()
        if i in ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']:
            lst.append(i)
    n = len(lst)
    if n == 0:
        rst.config(text = "plz enter a letter")
        return
    chk = 0
    if n%2 == 1:
        for j in range(int((n-1)/2)):
            if lst[j] == lst[-(j+1)]:
                chk += 1
        if chk == (n-1)/2:
            rst.config(text = "True")
        elif chk != (n-1)/2:
            rst.config(text = "False")
    elif n%2 == 0:
        for j in range(int(n/2)):
            if lst[j] == lst[-(j+1)]:
                chk += 1
        if chk == n/2:
            rst.config(text = "True")
        elif chk != n/2:
            rst.config(text = "False")
    return

tk = Tk()

tk.title("isPalindrome")

a1 = Label(tk, text = 'Enter a letter')
a1.grid(row = 0 , column = 0)

st = StringVar()
et = Entry(tk, textvariable = st)
et.grid(row = 0,column = 1)

rst = Label(tk)
rst.grid(row = 1,column = 1)

show_rst = partial(check,rst,st)

bt = Button(tk,text = 'show result', command = show_rst)
bt.grid(row = 1,column = 0)

tk.mainloop()
