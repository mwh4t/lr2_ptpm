from tkinter import *
from tkmacosx import Button, CircleButton
from other.params import (BTN_CONFIG, CIRCLE_BTN_CONFIG,
                          TEXT_CONFIG, LINE_CONFIG)
from other.widgets_handler import clear_widgets_func
# import re


def menu2_func(root, line_pic, back_btn_pic, w_back_btn_pic, equations_image,
               gh_image, w_gh_image, next_btn_pic, w_next_btn_pic):
    """
    Функция меню следующего раздела
    """
    def calc_btn_func(event):
        """
        Функция кнопки "Вычислить"
        """
        try:
            N = int(Nent.get())
            arr = list(map(int, arrent.get().split()))

            if len(arr) != N:
                ans_lbl.config(text=f"Вы ввели {len(arr)} элементов, вместо {N}!")
                ans_lbl.place(x=250, y=420)
            else:
                occurrences = {}  # словарь для хранения количества вхождений

                for num in arr:
                    if num in occurrences:
                        occurrences[num] += 1
                    else:
                        occurrences[num] = 1

                result_str = "\n".join(
                    [f"Элемент {num}: {count} раз" for num, count in occurrences.items()])
                ans_lbl.config(text=result_str)
                ans_lbl.place(x=320, y=420)
        except ValueError:
            ans_lbl.config(text="Некорректный ввод!")
            ans_lbl.place(x=300, y=420)

    def back_btn_func():
        """
        Функция для перехода на предыдущий раздел
        """
        clear_widgets_func([title, Nlbl, Nent, arrlbl, arrent,
                            line_lbl, calc_btn, back_btn, ans_lbl])

        from other.menu1 import menu1_func
        menu1_func(root, equations_image, line_pic,
                   gh_image, w_gh_image, next_btn_pic,
                   w_next_btn_pic, back_btn_pic,
                   w_back_btn_pic)

    # текст "число вхождений в массив:"
    title = Label(text="Число вхождений в массив:",
                  **TEXT_CONFIG)
    title.config(font="Helvetica 24")
    title.place(x=240, y=16)

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

    # кнопка перехода на предыдущий раздел
    back_btn = CircleButton(image=back_btn_pic, activeimage=w_back_btn_pic,
                            **CIRCLE_BTN_CONFIG, command=lambda: back_btn_func())
    back_btn.place(x=760, y=555)
