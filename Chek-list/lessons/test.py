from tkinter import *

class MainApp(Tk):
    def __init__(self, *arg, **kwarg):
        super().__init__(*arg, **kwarg)

        label = Label(self, text='First Window')
        button = Button(self, text='Open Window', command=self.new_window)

        label.pack()
        button.pack()

    def new_window(self):
        Window().mainloop()


class Window(Tk):
    def __init__(self, *arg, **kwarg):
        super().__init__(*arg, **kwarg)

        label = Label(self, text='Second Window')
        label.pack()


if __name__ == '__main__':
    MainApp().mainloop()
    MainApp().new_window()