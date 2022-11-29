from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
"""
root = Tk()     #Переменная, которая содержит в себе конструктор для создания окна Tk()
"""
"""
Ниже добавляются необходимые компоненты
"""


root = Tk()

title_name = "Check-list (v.0)"
root.title(title_name)      #метод title() устанавливает заголовок окна

label = Label(root, text="Дання программа является результатом прохождения бесплатного курса")  #Создает поле с текстом и помещает его в переменную
label.pack()    #отображает поле с текстом в окне

button_accept = Button(root, text="Принять")    #Создает кнопку
button_accept.pack()    #отображает кнопку

button_denied = Button(root, text="Отколнить") 
button_denied.pack()    #отображает кнопку

root.update_idletasks()     # Обновляем инфо об окне
screenwidth = root.winfo_screenwidth()      #Позволяет определить ширину экрана
screenheight = root.winfo_screenheight()      #Позволяет определить ширину экрана
screen_options = root.geometry().split('+')[0].split('x')       #Позволяет получить список параметров окна в формате [ширина, высота, координата X, координата Y]
width_root = int(screen_options[0])     #Позволяет получить ширину окна
height_root = int(screen_options[1])        #Позволяет получить высоту окна

root.geometry(f'{width_root}x{height_root}+{screenwidth // 2 - (width_root // 2)}+{screenheight // 2 - (height_root // 2)}')        #метод geometry() устанавливает размер окна (в аргументе "Ширина х Высота")

root.mainloop()     #Создает бесконечный цикл, который отвечает за запуск программы

