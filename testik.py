d = int(input())
m = int(input())
if m > 0 and m < 13 and d > 0 and d < 32:
    if m == 1:
        if d != 31:
            print(d+1, "Января")
        else:
            print(1, "Февраля")
    elif m == 3:
        if d != 31:
            print(d+1, "Марта")
        else:
            print(1, "Апреля")
    elif m == 5:
        if d != 31:
            print(d+1, "Мая")
        else:
            print(1, "Июня")
    elif m == 7:
        if d != 31:
            print(d+1, "Июля")
        else:
                print(1, "Августа")
    elif m == 8:
        if d != 31:
            print(d+1, "Августа")
        else:
            print(1, "Сентября")
    elif m == 10:
        if d != 31:
            print(d+1, "Октября")
        else:
              print(1, "Ноября")
    elif m == 12:
        if d != 31:
            print(d+1, "Декабря")
        else:
            print(1, "Января")
    elif m == 4:
        if d != 30:
            print(d+1, "Апреля")
        else:
            print(1, "Мая")
    elif m == 6:
        if d != 30:
            print(d+1, "Июня")
        else:
            print(1, "Июля")
    elif m == 9:
        if d != 30:
            print(d+1, "Сентября")
        else:
            print(1, "Октября")
    elif m == 11:
        if d != 30:
            print(d+1, "Ноября")
        else:
            print(1, "Декабря")
    else:
        if m == 2:
            if d != 28:
                print(d+1, "Февраля")
            else:
                print(1, "Марта")
        else:
            print("Неверная дата")
else:
    print("Неверная дата")