from tkinter import *
"""
root = Tk()     #Переменная, которая содержит в себе конструктор для создания окна Tk()
"""
"""
Ниже добавляются необходимые компоненты
"""

def create_window(center, name):

    root = Tk()

    screenwidth = root.winfo_screenwidth()      #Позволяет определить ширину экрана
    screenheight = root.winfo_screenheight()      #Позволяет определить ширину экрана
    screen_options = root.geometry().split('+')[0].split('x')       #Позволяет получить список параметров окна в формате [ширина, высота, координата X, координата Y]
    width_root = int(screen_options[0])     #Позволяет получить ширину окна
    height_root = int(screen_options[1])        #Позволяет получить высоту окна

    root.title(name)      #метод title() устанавливает заголовок окна
    match center:
        case "center":
            root.geometry(f'{width_root}x{height_root}+{screenwidth // 2}+{screenheight // 2}')        #метод geometry() устанавливает размер окна (в аргументе "Ширина х Высота")
        case "Top":
            root.geometry(f'{width_root}x{height_root}+{screenwidth // 2}+{0}')        #метод geometry() устанавливает размер окна (в аргументе "Ширина х Высота")
        case "Bottom":
            root.geometry(f'{width_root}x{height_root}+{screenwidth // 2}+{screenheight}')        #метод geometry() устанавливает размер окна (в аргументе "Ширина х Высота")
        case "Right":
            root.geometry(f'{width_root}x{height_root}+{0}+{screenheight // 2}')        #метод geometry() устанавливает размер окна (в аргументе "Ширина х Высота")
        case "Left":
            root.geometry(f'{width_root}x{height_root}+{screenwidth}+{screenheight // 2}')        #метод geometry() устанавливает размер окна (в аргументе "Ширина х Высота")
        case "Top-right":
            root.geometry(f'{width_root}x{height_root}+{0}+{0}')        #метод geometry() устанавливает размер окна (в аргументе "Ширина х Высота")
        case "Top-left":
            root.geometry(f'{width_root}x{height_root}+{0}+{screenheight}')
        case "Bottom-right":
            root.geometry(f'{width_root}x{height_root}+{screenwidth}+{0}')
        case "Bottom-left":
            root.geometry(f'{width_root}x{height_root}+{screenwidth}+{screenheight}')

    root.mainloop()     #Создает бесконечный цикл, который отвечает за запуск программы