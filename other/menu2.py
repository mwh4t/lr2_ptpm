from tkinter import *
from tkinter import Scrollbar
from tkmacosx import Button, CircleButton
from other.params import (BTN_CONFIG, CIRCLE_BTN_CONFIG,
                          TEXT_CONFIG, LINE_CONFIG)
from other.widgets_handler import clear_widgets_func


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
            n = int(nent.get())
            arr = list(map(int, arrent.get().split()))

            if len(arr) != n:
                ans_text.delete(1.0, END)
                ans_text.insert(END, f"Вы ввели {len(arr)} элементов, вместо {n}!")
                ans_text.place(x=282, y=300)
            else:
                occurrences = {}  # словарь для хранения количества вхождений

                for num in arr:
                    if num in occurrences:
                        occurrences[num] += 1
                    else:
                        occurrences[num] = 1

                result_str = " ".join(
                    [f"Эл. {num} - {count} раз;" for num, count in occurrences.items()])
                ans_text.delete(1.0, END)
                ans_text.insert(END, result_str)
                ans_text.place(x=282, y=300)
        except ValueError:
            ans_text.delete(1.0, END)
            ans_text.insert(END, "Некорректный ввод!")
            ans_text.place(x=300, y=300)

    def back_btn_func():
        """
        Функция для перехода на предыдущий раздел
        """
        clear_widgets_func([title, nlbl, nent, arrlbl, arrent,
                            line_lbl, calc_btn, back_btn, ans_text, scrollbar])

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
    nlbl = Label(text="Размер массива N:",
                 **TEXT_CONFIG)
    nlbl.place(x=100, y=200)
    # поле ввода для N
    nent = Entry()
    nent.place(x=100, y=250)

    # текст "элементы массива:"
    arrlbl = Label(text="Элементы массива:",
                   **TEXT_CONFIG)
    arrlbl.place(x=500, y=200)
    # поле ввода для массива
    arrent = Entry()
    arrent.place(x=500, y=250)

    # текст с ответом
    ans_text = Text(root, wrap=NONE, width=20, height=10, **TEXT_CONFIG)
    ans_text.place(x=300, y=300)

    # полоса прокрутки для текста с ответом
    scrollbar = Scrollbar(command=ans_text.xview, orient=HORIZONTAL)
    scrollbar.place(x=280, y=330, width=242, height=10)
    ans_text.configure(xscrollcommand=scrollbar.set)

    # картинка с линией
    line_lbl = Label(image=line_pic, **LINE_CONFIG)
    line_lbl.place(x=270, y=325)

    # кнопка "вычислить"
    calc_btn = Button(text="Вычислить", **BTN_CONFIG,
                      command=lambda event=None: calc_btn_func(event))
    calc_btn.place(x=330, y=550)
    root.bind("<KeyPress-Return>", calc_btn_func)  # по нажатию Enter

    # кнопка перехода на предыдущий раздел
    back_btn = CircleButton(image=back_btn_pic, activeimage=w_back_btn_pic,
                            **CIRCLE_BTN_CONFIG, command=lambda: back_btn_func())
    back_btn.place(x=760, y=555)
