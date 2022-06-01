# -*- coding: utf-8 -*-
"""
Created on Tue Mar 22 18:38:29 2022

@author: anees
"""

from tkinter import *
import random

root=Tk()
root.title("Dictionary")
root.geometry("400x400")

dictionary = {"colors" : ["maroon1","lawn green","magenta2","purple1","springgreen2","chocolate1", "deep pink","cyan"]}

def random():
    randomNo = random.randint(0,7)
    print(dictionary["colors"][randomNo])
    root.configure(background=dictionary["colors"][randomNo])
    
button = Button(root, "Click Me", command=random)
button.place(relx=0.5,rely=0.5,anchor=CENTER)

root.mainloop()