from tkinter import *

#Объявление функций для кнопок
def minus():
    label["text"] = float(ch1.get())-float(ch2.get())
def plus():
    label["text"] = float(ch1.get())+float(ch2.get())
def umnozh():
    label["text"] = float(ch1.get())*float(ch2.get())
def razdel():
    label["text"] = float(ch1.get())/float(ch2.get())

#Создание окна
win = Tk()
win.title("Calculator")
win.geometry("400x400")

#Объявление виджетов
ch1 = Entry()
ch2 = Entry()

btn1 = Button(text="+", command=plus)
btn2 = Button(text="-", command=minus)
btn3 = Button(text="*", command=umnozh)
btn4 = Button(text="/", command=razdel)

label = Label()

#Сборка виджетов
ch1.pack(anchor=NW, padx=4, pady=8)
ch2.pack(anchor=NW, padx=4, pady=8)

btn1.pack(anchor=NW, padx=3, pady=3)
btn2.pack(anchor=NW, padx=3, pady=3)
btn3.pack(anchor=NW, padx=3, pady=3)
btn4.pack(anchor=NW, padx=3, pady=3)

label.pack(anchor=NW, padx=8, pady=8)

win.mainloop()
