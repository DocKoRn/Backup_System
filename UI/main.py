import tkinter as tk
from tkinter import ttk
import mainwindow as mw


        

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



########################
##BUTTONS
########################

cmd_switch_editframe = ttk.Button(root, text='Edit')
cmd_switch_editframe.grid(row=0,column=3, sticky='nsew')

cmd_switch_baseframe = ttk.Button(root, text='Main')
cmd_switch_baseframe.grid(row=0,column=3,sticky='nsew')



#########################
#END
#########################
root.mainloop()