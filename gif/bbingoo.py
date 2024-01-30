import tkinter as tk
from tkinter import *
from tkinter import messagebox
import random
import socket

removed_numbers=[]
def numberClick(num,btn):
    messagebox.showinfo('Message',str(num)+' is removed')
    removed_numbers.append(num)
    btn.configure(text='X')
    btn.configure(bg='red',fg='white')
    btn.configure(state="disabled")
    print(removed_numbers)
root = Tk()
#root.geometry("200x200")
w = Label(root, text='Welcome to Bingo!') 
linear_array = [i for i in range(1,26)]
random_array = []
for i in range(1,26):
    temp = random.choice(linear_array)
    linear_array.remove(temp)
    random_array.append(temp) 

rows=5
columns=5
btns = [[None for i in range(rows)] for j in range(columns)]

xarray = 10
yarray = 10
count = 0
for i in range(rows):
    for j in range(columns):
        num = random.choice(random_array)
        random_array.remove(num)
        btns[i][j]=Button(root, text = num , fg ='red',height = 3, width = 5)
        btns[i][j]['command']=lambda btn=btns[i][j],num=num: numberClick(num,btn)
        btns[i][j].place(x= xarray, y= yarray)
        xarray = xarray + 45
        count = count + 1
        if count % 5 == 0:
            xarray = xarray - 225
            yarray = yarray + 55

#text1=Text(root,width=47,height=1,bg='grey')
#text1.grid(row=5,column=2)
root.mainloop() 
