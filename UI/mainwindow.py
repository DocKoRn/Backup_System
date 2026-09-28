import tkinter as tk
from tkinter import ttk

########################
#METHODS
########################



########################
#ROOT AND FRAMES
########################

root = tk.Tk()
root.geometry('800x600')
root.title('Backup System')


style = ttk.Style()
style.theme_use('clam')

BackupBaseFrame = ttk.Frame(root)
BackupBaseFrame.grid(row=0, column=0, padx=20, pady=30)


#########################
#WIDGETS
#########################






#########################
#END
#########################
root.mainloop()