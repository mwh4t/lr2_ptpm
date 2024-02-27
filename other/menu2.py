from tkinter import *
from tkmacosx import Button, CircleButton
from other.params import (BTN_CONFIG, CIRCLE_BTN_CONFIG, TEXT_CONFIG,
                          EQUATIONS_CONFIG, LINE_CONFIG)
# from other.widgets_handler import clear_widgets_func
# from other.menu1 import menu1_func
# import re


def menu2_func(root, line_pic):
    """
    Функция меню следующего раздела
    """
    def calc_btn_func(event):
        """
        Функция кнопки "Вычислить"
        """
        occurrences = {}

    # текст "число вхождений в массив:"
    title = Label(text="Число вхождений в массив:",
                  **TEXT_CONFIG)
    title.config(font="Helvetica 24")
    title.place(x=250, y=16)

    # текст "размер массива N:"
    Nlbl = Label(text="Размер массива N:",
                 **TEXT_CONFIG)
    Nlbl.place(x=100, y=200)
    # поле ввода для N
    Nent = Entry()
    Nent.place(x=100, y=250)

    # текст "элементы массива:"
    arrlbl = Label(text="Элементы массива:",
                   **TEXT_CONFIG)
    arrlbl.place(x=500, y=200)
    # поле ввода для массива
    arrent = Entry()
    arrent.place(x=500, y=250)

    # картинка с линией
    line_lbl = Label(image=line_pic, **LINE_CONFIG)
    line_lbl.place(x=270, y=445)

    # кнопка "вычислить"
    calc_btn = Button(text="Вычислить", **BTN_CONFIG,
                      command=lambda event=None: calc_btn_func(event))
    calc_btn.place(x=330, y=550)
    root.bind("<KeyPress-Return>", calc_btn_func)  # по нажатию Enter
