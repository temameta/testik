from tkinter import *
from locator import Locator

#Объявление локатора
locator = Locator()

#Функции смены сторон света
def napravo():
    locator.povorot(1)
    otobrazhenie()
def nalevo():
    locator.povorot(2)
    otobrazhenie()
def na180():
    locator.povorot(3)
    otobrazhenie()
#Функция отображения стрелочек
def otobrazhenie():
    if locator.current_pos() == "С":
        labelCs["text"] = "↑"
        labelUs["text"] = ""
        labelZs["text"] = ""
        labelVs["text"] = ""
    elif locator.current_pos() == "Ю":
        labelCs["text"] = ""
        labelUs["text"] = "↓"
        labelZs["text"] = ""
        labelVs["text"] = ""
    elif locator.current_pos() == "З":
        labelCs["text"] = ""
        labelUs["text"] = ""
        labelZs["text"] = "←"
        labelVs["text"] = ""
    elif locator.current_pos() == "В":
        labelCs["text"] = ""
        labelUs["text"] = ""
        labelZs["text"] = ""
        labelVs["text"] = "→"

#Создание окна
win = Tk()
win.title("Locator")
win.geometry("200x200")

#Объявление виджетов сторон света
labelC = Label(text="Север")
labelU = Label(text="Юг")
labelZ = Label(text="Запад")
labelV = Label(text="Восток")
#Объявление виджетов для стрелочек
labelCs = Label(text="↑")
labelUs = Label(text="")
labelZs = Label(text="")
labelVs = Label(text="")

#Объявление кнопок
btn1 = Button(text="↺", command=nalevo,width=2)
btn3 = Button(text="⇄", command=na180, width=5)
btn2 = Button(text="↻", command=napravo, width=2)

#Расстановка кнопок на экране
btn1.place(x=0,y=175)
btn3.place(x=77,y=175)
btn2.place(x=176,y=175)

#Расстановка виджетов сторон света и стрелочек
#Север
labelC.place(x=75, y=10)
labelCs.place(x=88,y=25)
#Юг
labelU.place(x=80, y=150)
labelUs.place(x=86,y=130)
#Запад
labelZ.place(x=0,y=70)
labelZs.place(x=40,y=70)
#Восток
labelV.place(x=156,y=70)
labelVs.place(x=136,y=70)

win.mainloop()