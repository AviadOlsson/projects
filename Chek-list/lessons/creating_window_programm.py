from tkinter import *
"""
root = Tk()     #Переменная, которая содержит в себе конструктор для создания окна Tk()
"""
"""
Ниже добавляются необходимые компоненты
"""
root = Tk()
title_name = "Check-list (v.0)"

screenwidth = root.winfo_screenwidth()      #Позволяет определить ширину экрана
screenheight = root.winfo_screenheight()      #Позволяет определить ширину экрана
screen_options = root.geometry().split('+')[0].split('x')       #Позволяет получить список параметров окна в формате [ширина, высота, координата X, координата Y]
width_root = int(screen_options[0])     #Позволяет получить ширину окна
height_root = int(screen_options[1])        #Позволяет получить высоту окна
root.update_idletasks()     # Обновляем инфо об окне

root.title(title_name)      #метод title() устанавливает заголовок окна
    

root.geometry(f'{400}x{100}+{screenwidth // 2 - 200}+{screenheight // 2 - 50}')        #метод geometry() устанавливает размер окна (в аргументе "Ширина х Высота")
        
root.mainloop()     #Создает бесконечный цикл, который отвечает за запуск программы