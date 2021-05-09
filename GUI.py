from tkinter import *
# from tkinter.ttk import *
from tkinter import font
from tkinter.filedialog import askopenfile
import subprocess
# import PIL
from PIL import Image, ImageTk
import os
import tkinter as tk
import matching
import main
from multiprocessing import Process
import time

root = Tk()
root.geometry('1000x1000')
root.title("Content Based Search Engine")


# root.configure(bg='#fff')

def retrieve_input():
    user_input = textBox.get("1.0", "end-1c")
    FILEBROWSER_PATH = os.path.join(os.getenv('WINDIR'), 'explorer.exe')
    folder_path = os.path.normpath("dataset/" + str(user_input))
    subprocess.run([FILEBROWSER_PATH, folder_path])


def open_file():
    global path
    file = askopenfile(mode='r', filetypes=[('Query Image', '*.jpg')])

    if file is not None:
        path = file.name
        # print(path)
    open_file.img_path = path
    # print(open_file.img_path)

    addrc2 = Label()
    addrc2.pack(pady=50)
    canvas = tk.Canvas(width=200, height=200)
    canvas.pack()

    im = Image.open(open_file.img_path)
    width, height = im.size
    resized = im.resize((int(width / 2), int(height / 2)), Image.ANTIALIAS)
    img1 = ImageTk.PhotoImage(resized)

    canvas.create_text(100, 10, fill="maroon", font="Times 10 bold", text="QUERY IMAGE:")
    canvas.pack()
    # canvas.place(x=30, y=500)

    canvas.create_image((100, 110), image=img1, tag="Query Image", anchor="center")
    canvas.pack()

    btn2 = Button(root, text='Search', background='#F8F8FF', font=buttonFont, height=1, width=15,
                  foreground='#002b80', overrelief='sunken', command=lambda: matchmaking(open_file.img_path))
    btn2.pack(side=TOP, pady=10)

    mainloop()


def matchmaking(des):
    t0 = time.time()

    print("Des is::::::::")
    print(des)
    img_label = main.find(des)

    folder_name = ["01_test", "aeroplane", "bird", "boat", "car", "cat", "chair", "clock", "cup", "dog", "elephant",
                   "ewer", "laptop", "Motorbike", "person", "pizza", "scissors", "sports ball", "stop sign", "umbrella"]
    flag = 0
    for p in folder_name:
        if img_label == p:
            flag = flag + 1
            break
        else:
            flag = flag + 0

    if img_label is None or flag == 0:
        for i in range(len(folder_name)):
            match_found = matching.match_main(des, folder_name[i])
            match_len = len(match_found)

            # image_path = []
    else:
        print("Image Label: " + str(img_label))
        match_found = matching.match_main(des, img_label)
        match_len = len(match_found)

    image_path = []
    t1 = time.time() - t0
    print("Time for GUI matchmaking: " + str(t1))

    print("Total Matches found: " + str(match_len))

    canvas = tk.Canvas(root, width=600, height=30)
    canvas.pack()
    canvas.create_text(300, 20, fill="maroon", font="Times 10 bold", text="MATCHES FOUND: " + str(match_len))
    canvas.pack()

    for i in match_found:
        impath2 = str(i)
        impath3 = impath2.replace('.txt', '.jpg')
        impath4 = impath3.replace('_image_', '/image_')
        open_file.im_path = impath4
        image_path.append(open_file.im_path)
        # print(open_file.im_path)

    a = 430
    b = 630
    c = a - 200
    d = b
    z = 0
    e = 430
    f = e - 200

    for i in image_path:
        img = Image.open(i)

        width, height = img.size
        resized = img.resize((int(width / 2), int(height / 2)), Image.ANTIALIAS)
        img1 = ImageTk.PhotoImage(resized)

        i = Label(image=img1)
        i.image = img1

        if match_len == 0:
            break
        elif z % 2 == 0 and z < 6:
            i.place(x=a, y=b)
            a = a + 200
        elif z % 2 == 1 and z < 6:
            i.place(x=c, y=d)
            c = c - 200
        elif z % 2 == 0 and z > 5:
            b = 830
            i.place(x=e, y=b)
            e = e + 200
        elif z % 2 == 1 and z > 5:
            d = 830
            i.place(x=f, y=d)
            f = f - 200
        z = z + 1


        """""
        if match_len == 0:
            break
        else:
            if c == 0:
                i.place(x=a, y=b)
                a = a - 200
                c = c + 1
            elif c == 1:
                i.place(x=a, y=b)
                a = a + 400
                c = c + 1
            elif c == 2:
                i.place(x=a, y=b)
                a = a - 600
                c = c + 1
            elif c == 3:
                i.place(x=a, y=b)
                a = a + 800
                c = c + 1
            else:
                break
        """

    # ________________GUI_____________


ta = time.time()

tframe = Frame(root)
tframe.pack(side=TOP, pady=10, fill=X)
addrc = Label(tframe, text="CONTENT BASED SEARCH ENGINE", font="Times 20 bold")
addrc.pack(pady=10)

buttonFont = font.Font(family='roboto', size=11, )
cFont = font.Font(family='roboto', size=15)


def delete_text():
    textBox.delete("1.0", "end")


browse = Button(root, text='Browse Image', background='#F8F8FF', font=buttonFont, height=1, width=20,
                foreground='#002b80', overrelief='sunken', command=lambda: open_file())
browse.pack()

root.canvas = Canvas(root, width=200, height=30)
root.canvas.create_text(100, 13, font=cFont, text="or", )
root.canvas.pack()

textBox = Text(root, height=2, width=30, bg='#d9d9f2', font=buttonFont, )
textBox.insert(INSERT, "Enter Keyword...")
textBox.pack()

clear = Button(root, text="Clear", background='#F8F8FF', font=buttonFont, height=1, width=10,
               foreground='#002b80', overrelief='sunken',
               command=lambda: delete_text())
clear.pack()
clear.place(x=541, y=230)

search = Button(root, text="Search Image", background='#F8F8FF', font=buttonFont, height=1, width=12,
                foreground='#002b80', overrelief='sunken',
                command=lambda: retrieve_input())
search.pack()
search.place(x=348, y=231)

exit1 = Button(root, text="Exit", background='#F8F8FF', font=buttonFont, height=1, width=8,
               foreground='#ff0f00', overrelief='sunken', command=root.destroy)
exit1.pack()
exit1.place(x=465, y=280)

mainloop()

tb = time.time() - ta
print("Overall Time: " + str(tb))
