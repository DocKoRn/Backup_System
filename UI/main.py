import tkinter as tk
from tkinter import ttk
import mainwindow as mw

def switch_editframe():
    EditFrame1.tkraise()
    cmd_switch_baseframe.configure(state='enabled')
    cmd_switch_editframe.configure(state='disabled')
    cmd_switch_baseframe.tkraise()

def switch_baseframe():
    BaseFrame.tkraise()
    cmd_switch_baseframe.configure(state='disabled')
    cmd_switch_editframe.configure(state='enabled')
    cmd_switch_editframe.tkraise()
        

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

EditFrame1 = mw.EditFrame(root)
EditFrame1.grid(row=0, column=0, sticky='nsew', padx=10, pady=20)

BaseFrame = mw.BaseFrame(root)
BaseFrame.grid(row=0, column=0, sticky='nsew', padx=10, pady=20)

cmd_switch_baseframe = ttk.Button(root, text='Main', command=switch_baseframe)
cmd_switch_baseframe.grid(row=0,column=3,sticky='nsew')

cmd_switch_editframe = ttk.Button(root, text='Edit', command=switch_editframe)
cmd_switch_editframe.grid(row=0,column=3, sticky='nsew')

#########################
#END
#########################
root.mainloop()