# -*- coding: utf-8 -*-
"""
Created on Mon Jan 13 22:24:18 2020

@author: gabri
"""

from tkinter import *

root = Tk()

# Creating Label Widget
myLabel1 = Label(root, text = "Hello World!")
myLabel2 = Label(root, text = "My name is Gabriel H Riqueti")

# Shoving it onto the screen
myLabel1.grid(row = 0, column = 0)
myLabel2.grid(row = 1, column = 0)

root.mainloop()

