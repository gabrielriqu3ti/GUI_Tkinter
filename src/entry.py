# -*- coding: utf-8 -*-
"""
Created on Mon Jan 13 23:03:22 2020

@author: gabri
"""

from tkinter import *

root = Tk()

entry = Entry(root, width=60, borderwidth = 3,
          fg = "#33ee66", bg = "#111111")
entry.pack()
entry.insert(0, "Insert your name : ")

def myClick():
    myLabel = Label(root, text = f"Text : {entry.get()}")
    myLabel.pack()

myButton = Button(root, text = "Click me!",
                  command = myClick,
                  padx = 30, pady = 20,
                  fg = "#1155aa", bg = "#44ee99") # Try state = DISABLED
myButton.pack()

root.mainloop()

