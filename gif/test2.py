from tkinter import *
from tkinter import messagebox
import tkinter.font



def btnpress():
    bingo1.config(text = fillin1.get())
    bingo2.config(text = fillin2.get())
    bingo3.config(text = fillin3.get())
    bingo4.config(text = fillin4.get())
    bingo5.config(text = fillin5.get())
    bingo6.config(text = fillin6.get())
    bingo7.config(text = fillin7.get())
    bingo8.config(text = fillin8.get())
    bingo9.config(text = fillin9.get())
    
	


win = Tk()
win.geometry("1920x1080")       
win.title("빙고 판에 들어갈 것을 입력해주세요")


font = tkinter.font.Font(family = "UhBee Se_hyun", size = 22)

fillin1 = Entry(win)
fillin1.place(x=700, y=10, width = 50, height =50)
fillin2 = Entry(win)
fillin2.place(x=750, y =10, width = 50, height = 50)
fillin3 = Entry(win)
fillin3.place(x=800, y=10, width = 50, height = 50)
fillin4 = Entry(win)
fillin4.place(x=700, y=60, width = 50, height =50)
fillin5 = Entry(win)
fillin5.place(x=750, y=60, width = 50, height = 50)
fillin6 = Entry(win)
fillin6.place(x=800, y=60, width = 50, height = 50)
fillin7 = Entry(win)
fillin7.place(x=700, y = 110, width = 50, height = 50)
fillin8 = Entry(win)
fillin8.place(x=750, y = 110, width = 50, height = 50)
fillin9 = Entry(win)
fillin9.place(x=800, y = 110, width = 50, height = 50)




bing1 = Button(win, text = "입력")
bing1.place(x=750, y = 165)
bing1.config(command = btnpress)



bingo1 = Button(win, text = " ", anchor = CENTER, width=6, height =2, font = font)
bingo1.place(x = 150, y = 270)
