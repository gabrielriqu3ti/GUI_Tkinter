# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 18:23:12 2020

@author: gabri
"""

from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Image")

root.iconbitmap('./Images/batman.ico')

my_img1 = ImageTk.PhotoImage(Image.open("./Images/cat_or_dog_1.jpg"))
my_img2 = ImageTk.PhotoImage(Image.open("./Images/cat_or_dog_2.jpg"))
my_img3 = ImageTk.PhotoImage(Image.open("./Images/cat_or_dog_3.jpeg"))

image_list = [my_img1, my_img2, my_img3]

my_label = Label(image = my_img1)
my_label.grid(row = 0, column = 0, columnspan = 3)

def forward(img_id):
    global my_label
    global button_forward
    global button_back

    my_label.grid_forget()
    my_label = Label(image = image_list[img_id%3])

    button_forward = Button(root, text = ">>", command = lambda: forward((img_id+1)%3))
    button_back = Button(root, text = "<<", command = lambda: back((img_id-1)%3))

    my_label.grid(row = 0, column = 0, columnspan = 3)
    button_back.grid(row = 1, column = 0)
    button_exit.grid(row = 1, column = 1)
    button_forward.grid(row = 1, column = 2)

def back(img_id):
    global my_label
    global button_forward
    global button_back


button_back = Button(root, text = "<<", command = lambda: back(3))
button_exit = Button(root, text = "Exit", command = root.quit)
button_forward = Button(root, text = ">>", command = lambda: forward(1))

button_back.grid(row = 1, column = 0)
button_exit.grid(row = 1, column = 1)
button_forward.grid(row = 1, column = 2)

root.mainloop()