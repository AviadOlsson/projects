from tkinter import *
from tkinter import ttk

root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()
frm_title = ttk.Label(frm, text="Title")
lbl_title = Label(frm_title, text="The list title:").pack(side=LEFT)
list_title = Entry(frm_title).pack(side=LEFT, fill=X, expand=1)
frm_title.pack(fill=X)

root.mainloop()