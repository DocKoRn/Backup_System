import tkinter as tk
from tkinter import ttk
import mainwindow as mw

def add_baseframe():
    bf2 = mw.BaseFrame(root)
        

########################
#METHODS
########################



########################
#ROOT
########################
root = mw.MainWindow()

########################
#FRAMES
########################

BaseFrame = mw.BaseFrame(root)

cmd_add_bf = ttk.Button(root, text='add new frame', command=add_baseframe)
cmd_add_bf.grid(row=99,column=0,columnspan=2)

#########################
#END
#########################
root.mainloop()