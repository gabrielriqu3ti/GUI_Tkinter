# -*- coding: utf-8 -*-
"""
Created on Mon Jan 13 23:21:25 2020

@author: gabri
"""

from tkinter import *

root = Tk()
root.title("Simple Calculator")

entry = Entry(root, width = 35, borderwidth = 5)
entry.grid(row = 0, column = 0, columnspan = 3, padx = 10, pady = 10)

# Defines function of buttons

def button_click(number):
    current = entry.get()
    entry.delete(0, END) # delete all entries
    entry.insert(0, current + str(number))

def button_clear():
    entry.delete(0, END)

def button_add():
    global num1, operator
    operator = '+'
    number_1 = entry.get()
    num1 = int(number_1)
    entry.delete(0, END)
    
def button_sub():
    global num1, operator
    operator = '-'
    number_1 = entry.get()
    num1 = int(number_1)
    entry.delete(0, END)

def button_mul():
    global num1, operator
    operator = '*'
    number_1 = entry.get()
    num1 = int(number_1)
    entry.delete(0, END)

def button_div():
    global num1, operator
    operator = '/'
    number_1 = entry.get()
    num1 = int(number_1)
    entry.delete(0, END)


def button_equal():
    num2 = int(entry.get())
    entry.delete(0, END)
    if (operator == '+'):
        entry.insert(0, num1 + num2)
    elif (operator == '-'):
        entry.insert(0, num1 - num2)
    elif (operator == '*'):
        entry.insert(0, num1 * num2)
    elif (operator == '/'):
        entry.insert(0, num1 / num2)


# Define buttons

# Numbers
button_0 = Button(root, text="0", padx = 40, pady = 20, command = lambda: button_click(0))
button_1 = Button(root, text="1", padx = 40, pady = 20, command = lambda: button_click(1))
button_2 = Button(root, text="2", padx = 40, pady = 20, command = lambda: button_click(2))
button_3 = Button(root, text="3", padx = 40, pady = 20, command = lambda: button_click(3))
button_4 = Button(root, text="4", padx = 40, pady = 20, command = lambda: button_click(4))
button_5 = Button(root, text="5", padx = 40, pady = 20, command = lambda: button_click(5))
button_6 = Button(root, text="6", padx = 40, pady = 20, command = lambda: button_click(6))
button_7 = Button(root, text="7", padx = 40, pady = 20, command = lambda: button_click(7))
button_8 = Button(root, text="8", padx = 40, pady = 20, command = lambda: button_click(8))
button_9 = Button(root, text="9", padx = 40, pady = 20, command = lambda: button_click(9))

# Operators
button_add   = Button(root, text="+", padx = 40, pady = 20, command = button_add)
button_sub   = Button(root, text="-", padx = 40, pady = 20, command = button_sub)
button_mul   = Button(root, text="*", padx = 40, pady = 20, command = button_mul)
button_div   = Button(root, text="/", padx = 40, pady = 20, command = button_div)
button_equal = Button(root, text="=", padx = 40, pady = 20, command = button_equal)
button_clear = Button(root, text="Clear", padx = 30, pady = 20, command = button_clear)

# Put buttons on the screen

button_7.grid(row = 1, column = 0)
button_8.grid(row = 1, column = 1)
button_9.grid(row = 1, column = 2)
button_add.grid(row = 1, column = 3)

button_4.grid(row = 2, column = 0)
button_5.grid(row = 2, column = 1)
button_6.grid(row = 2, column = 2)
button_sub.grid(row = 2, column = 3)

button_1.grid(row = 3, column = 0)
button_2.grid(row = 3, column = 1)
button_3.grid(row = 3, column = 2)
button_mul.grid(row = 3, column = 3)

button_clear.grid(row = 4, column = 0)
button_0.grid(row = 4, column = 1)
button_equal.grid(row = 4, column = 2)
button_div.grid(row = 4, column = 3)


#myButton = Button(root, text = "Click me!",
#                  command = myClick,
#                  padx = 30, pady = 20,
#                  fg = "#1155aa", bg = "#44ee99") # Try state = DISABLED
#myButton.pack()




root.mainloop()
