"""
1. Даны числа a1, b1, c1, a2, b2, c2. Напечатать координаты точки пересечения прямых,
описываемых уравнениями a1x+b1y=c1 и a2x+b2y=c2, либо сообщить, что эти прямые совпадают,
не пересекаются или вовсе не существуют.

2. Даны натуральное число N и одномерный массив A1, A2, …, AN натуральных чисел.
Для каждого элемента определить число его вхождений в данный массив.

Тестировать методом комбинаторного покрытия условий (2.5)
"""

from tkinter import *
from other.menu1 import menu1_func


# создание основного окна
root = Tk()
root.title("Точки пересечения прямых")
root.geometry("800x600")
root.geometry("+300+100")
root.resizable(False, False)

# цвет фона
root.configure(bg="#262626")

# изображения с уравнениями
equations_image = PhotoImage(file="other/pics/equations.png")

# изображение с линией
line_pic = PhotoImage(file="other/pics/line.png")

# изображения с ГитХабом
gh_image = PhotoImage(file="other/pics/gh.png")
w_gh_image = PhotoImage(file="other/pics/w_gh.png")

# функция главного меню
menu1_func(root, equations_image, line_pic,
           gh_image, w_gh_image)

# запуск основного цикла
root.mainloop()
