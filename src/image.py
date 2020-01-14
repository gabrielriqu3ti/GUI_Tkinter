# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 00:37:33 2020

@author: gabri
"""

from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Image")

root.iconbitmap('../Images/batman.ico')

my_img = ImageTk.PhotoImage(Image.open("../Images/cat_or_dog_3.jpeg"))
my_label = Label(image = my_img)
my_label.pack()

button_quit = Button(root, text = "Exit", command=root.quit)
button_quit.pack()



root.mainloop()
