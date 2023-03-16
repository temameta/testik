from tkinter import *
from locator import Locator

locator = Locator()

def napravo():
    locator.povorot(1)
    label["text"] = locator.current_pos()
def nalevo():
    locator.povorot(2)
    label["text"] = locator.current_pos()
def na180():
    locator.povorot(3)
    label["text"] = locator.current_pos()

win = Tk()
win.title("Locator")
win.geometry("200x200")

labelC = Label(text="Север")
labelU = Label(text="Юг")
labelZ = Label(text="Запад")
labelV = Label(text="Восток")
labelCs = Label(text="Север")
labelUs = Label(text="Юг")
labelZs = Label(text="Запад")
labelVs = Label(text="Восток")

btn1 = Button(text="<-", command=nalevo)
btn3 = Button(text="<- ->", command=na180)
btn2 = Button(text="->", command=napravo)

btn1.place(x=0,y=175)
btn3.place(x=80,y=175)
btn2.place(x=176,y=175)

labelC.place(x=176, y=20)
labelU.place(x=176, y=150)
labelZ.place(x=0, y=70)
labelV.place(x=176, y=70)

win.mainloop()
