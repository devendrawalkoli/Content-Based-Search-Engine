from tkinter import *
from tkinter.ttk import *
from tkinter.filedialog import askopenfile
from PIL import Image, ImageTk
import os

root = Tk()
root.geometry('1000x1000')
path = ''

tframe = Frame(root)
tframe.pack(side=TOP, pady=10, fill=X)
addrc = Label(tframe, text="CONTENT BASED SEARCH ENGINE", font=('bold'))
addrc.pack(pady=10)


def open_file():
    file = askopenfile(mode='r', filetypes=[('Query Image', '*.jpg')])

    if file is not None:
        global path
        path = file.name
        print(path)


btn = Button(root, text='Browse Image', command=lambda: open_file())
btn.pack(side=TOP, pady=10)

mainloop()






