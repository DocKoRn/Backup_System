import tkinter as tk
from tkinter import ttk

########################
#METHODS
########################



########################
#ROOT
########################
root = tk.Tk()
root.geometry('800x600')
root.title('Backup System')
root.columnconfigure(0, weight=2)
root.rowconfigure(0, weight=5)
root.rowconfigure(1, weight=1)
########################
#FRAMES
########################

BaseFrame = ttk.Frame(root, relief='sunken', border=1)
BaseFrame.grid(sticky='nsew', padx=10, pady=20)
BaseFrame.columnconfigure(0, weight=1)
BaseFrame.columnconfigure(1, weight=1)
BaseFrame.columnconfigure(2, weight=1)

BaseButtonFrame = ttk.Frame(BaseFrame)
BaseButtonFrame.grid(row=0, column=0, sticky='nsew')

BaseFillerFrame = ttk.Frame(BaseFrame)
BaseFillerFrame.grid(row=0, column=1, sticky='nsew')

BaseLabelFrame = ttk.Frame(BaseFrame)
BaseLabelFrame.grid(row=0, column=2, sticky='nsew')

########################
#STYLE
########################
# style = ttk.Style()
# style.theme_use('clam')


#########################
#WIDGETS
#########################

#########
#Buttons
#########
cmdRemoveTxt = tk.StringVar()
cmdRemoveTxt.set('Remove')
cmdRemove = ttk.Button(BaseButtonFrame, textvariable=cmdRemoveTxt)
cmdRemove.grid(column=0, row=0)

cmdEditTxt = tk.StringVar()
cmdEditTxt.set('Edit')
cmdEdit = ttk.Button(BaseButtonFrame, textvariable=cmdEditTxt)
cmdEdit.grid(column=0, row=1)

cmdBackupTxt = tk.StringVar()
cmdBackupTxt.set('Backup\nNow')
cmdBackup = ttk.Button(BaseButtonFrame, textvariable=cmdBackupTxt)
cmdBackup.grid(column=1, row=0, rowspan=2, sticky='nsew')

#########
#Labels
#########

LblInfoBoxTopTxt = tk.StringVar()
LblInfoBoxTopTxt.set('InfoBox:')
LblInfoBoxTop = ttk.Label(BaseLabelFrame, textvariable=LblInfoBoxTopTxt)
LblInfoBoxTop.grid(row=0, column=0, sticky='ew')


LblInfoBoxTxt = tk.StringVar()
LblInfoBoxTxt.set('Last Backup: Today')
LblInfoBox = ttk.Label(BaseLabelFrame, textvariable=LblInfoBoxTxt, background='beige')
LblInfoBox.grid(row=1, column=0, sticky='ew')


#########################
#END
#########################
root.mainloop()