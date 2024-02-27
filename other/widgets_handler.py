def clear_widgets_func(widgets):
    """
    Функция для очистки всех виджетов
    """
    for widget in widgets:
        widget.place_forget()
