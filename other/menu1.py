from tkinter import *
from tkmacosx import Button, CircleButton
from other.params import (BTN_CONFIG, CIRCLE_BTN_CONFIG, TEXT_CONFIG,
                          EQUATIONS_CONFIG, LINE_CONFIG)
from other.widgets_handler import clear_widgets_func
from other.menu2 import menu2_func
import re
import webbrowser


def menu1_func(root, equations_image, line_pic,
               gh_image, w_gh_image):
    """
    Функция главного меню
    """
    pattern = r"^-?\d{1,3}(\.\d{1,3})?$"

    def calc_btn_func(event):
        """
        Функция кнопки "Вычислить"
        """
        if (not re.match(pattern, a1ent.get()) or not re.match(pattern, b1ent.get())
                or not re.match(pattern, c1ent.get()) or not re.match(pattern, a2ent.get())
                or not re.match(pattern, b2ent.get()) or not re.match(pattern, c2ent.get())):
            ans_lbl.config(text="Некорректный ввод!",
                           **TEXT_CONFIG)
            ans_lbl.place(x=300, y=420)
            return

        try:
            a1 = float(a1ent.get())
            b1 = float(b1ent.get())
            c1 = float(c1ent.get())

            a2 = float(a2ent.get())
            b2 = float(b2ent.get())
            c2 = float(c2ent.get())

            determinant = a1 * b2 - a2 * b1

            if determinant == 0:
                # прямые совпадают или параллельны
                if a1 / a2 == b1 / b2 == c1 / c2:
                    ans_lbl.config(text="Прямые совпадают")
                    ans_lbl.place(x=310, y=420)
                else:
                    ans_lbl.config(text="Прямые параллельны и не пересекаются")
                    ans_lbl.place(x=220, y=420)
            else:
                # находим координаты точки пересечения
                x = round(((c1 * b2 - c2 * b1) / determinant), 2)
                y = round(((a1 * c2 - a2 * c1) / determinant), 2)
                ans_lbl.config(text=f"{x}, {y}")
                ans_lbl.place(x=350, y=420)
        except ZeroDivisionError:
            ans_lbl.config(text="Деление на ноль. Прямые параллельны и не пересекаются.")
            ans_lbl.place(x=355, y=420)

    def next_btn_func():
        """
        Функция для перехода на следующий раздел
        """
        clear_widgets_func([title, equations, a1lbl, a1ent, b1lbl, b1ent,
                           c1lbl, c1ent, a2lbl, a2ent, b2lbl, b2ent,
                           c2lbl, c2ent, ans_lbl, line_lbl, calc_btn,
                           next_btn])

        menu2_func(root, line_pic)

    def gh_btn_func():
        """
        Функция для открытия моего профиля ГитХаба))
        """
        webbrowser.open("https://github.com/mwh4t")

    # текст "точки пересечения прямых:"
    title = Label(text="Точки пересечения прямых:",
                  **TEXT_CONFIG)
    title.config(font="Helvetica 24")
    title.place(x=250, y=16)

    # картинка с уравнениями
    equations = Label(image=equations_image,
                      **EQUATIONS_CONFIG)
    equations.place(x=90, y=80)

    # текст "a₁ ="
    a1lbl = Label(text="a₁ =", **TEXT_CONFIG)
    a1lbl.place(x=100, y=207)
    # поле ввода для a₁
    a1ent = Entry()
    a1ent.place(x=140, y=210)
    # текст "b₁ ="
    b1lbl = Label(text="b₁ =", **TEXT_CONFIG)
    b1lbl.place(x=100, y=257)
    # поле ввода для b₁
    b1ent = Entry()
    b1ent.place(x=140, y=260)
    # текст "c₁ ="
    c1lbl = Label(text="c₁ =", **TEXT_CONFIG)
    c1lbl.place(x=100, y=307)
    # поле ввода для c₁
    c1ent = Entry()
    c1ent.place(x=140, y=310)

    # текст "a₂ ="
    a2lbl = Label(text="a₂ =", **TEXT_CONFIG)
    a2lbl.place(x=430, y=207)
    # поле ввода для a₂
    a2ent = Entry()
    a2ent.place(x=470, y=210)
    # текст "b₂ ="
    b2lbl = Label(text="b₂ =", **TEXT_CONFIG)
    b2lbl.place(x=430, y=257)
    # поле ввода для b₂
    b2ent = Entry()
    b2ent.place(x=470, y=260)
    # текст "c₂ ="
    c2lbl = Label(text="c₂ =", **TEXT_CONFIG)
    c2lbl.place(x=430, y=307)
    # поле ввода для c₂
    c2ent = Entry()
    c2ent.place(x=470, y=310)

    # текст с ответом
    ans_lbl = Label(text="", **TEXT_CONFIG)
    ans_lbl.place(x=300, y=420)

    # картинка с линией
    line_lbl = Label(image=line_pic, **LINE_CONFIG)
    line_lbl.place(x=270, y=445)

    # кнопка "вычислить"
    calc_btn = Button(text="Вычислить", **BTN_CONFIG,
                      command=lambda event=None: calc_btn_func(event))
    calc_btn.place(x=330, y=550)
    root.bind("<KeyPress-Return>", calc_btn_func)  # по нажатию Enter

    # кнопка перехода на следующий раздел
    next_btn = Button(text="Дальше", **BTN_CONFIG,
                      command=lambda: next_btn_func())
    next_btn.place(x=680, y=555)

    # кнопка-ссылка на ГитХаб
    gh_btn = CircleButton(image=gh_image, activeimage=w_gh_image,
                          **CIRCLE_BTN_CONFIG, command=lambda: gh_btn_func())
    gh_btn.place(x=8, y=555)
