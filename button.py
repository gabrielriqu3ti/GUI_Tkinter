# -*- coding: utf-8 -*-
"""
Created on Mon Jan 13 22:33:17 2020

@author: gabri
"""

from tkinter import *

root = Tk()

def myClick():
    myLabel = Label(root, text="Clicked here!")
    myLabel.pack()

myButton = Button(root, text = "Click me!",
                  command = myClick,
                  padx = 30, pady = 20,
                  fg = "#1155aa", bg = "#44ee99") # Try state = DISABLED
myButton.pack()

root.mainloop()

