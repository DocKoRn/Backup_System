import tkinter as tk
from tkinter import ttk
import mainframemethods as mfm

class MainWindow(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry('800x600')
        self.title('Backup System')
        self.columnconfigure(0, weight=2)
        self.rowconfigure(0, weight=5)
        self.rowconfigure(1, weight=1)
        
class BaseFrame(mfm.BaseFrameMethods):
    def __init__(self,container, **kwargs):
        super().__init__(container,**kwargs)
        self.configure(relief='sunken',border=1)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)
        self.grid(sticky='nsew', padx=10, pady=20)
        
        BaseButtonFrame = ttk.Frame(self)
        BaseButtonFrame.grid(row=0, column=0, sticky='nsew')

        BaseFillerFrame = ttk.Frame(self)
        BaseFillerFrame.grid(row=0, column=1, sticky='nsew')

        BaseLabelFrame = ttk.Frame(self)
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
        self.cmdRemoveTxt = tk.StringVar()
        self.cmdRemoveTxt.set('Remove')
        cmdRemove = ttk.Button(BaseButtonFrame, textvariable=self.cmdRemoveTxt, command=self.handle_cmdRemove)
        cmdRemove.grid(column=0, row=0)

        self.cmdEditTxt = tk.StringVar()
        self.cmdEditTxt.set('Edit')
        cmdEdit = ttk.Button(BaseButtonFrame, textvariable=self.cmdEditTxt)
        cmdEdit.grid(column=0, row=1)

        self.cmdBackupTxt = tk.StringVar()
        self.cmdBackupTxt.set('Backup\nNow')
        cmdBackup = ttk.Button(BaseButtonFrame, textvariable=self.cmdBackupTxt)
        cmdBackup.grid(column=1, row=0, rowspan=2, sticky='nsew')

        #########
        #Labels
        #########

        self.LblInfoBoxTopTxt = tk.StringVar()
        self.LblInfoBoxTopTxt.set('InfoBox:')
        LblInfoBoxTop = ttk.Label(BaseLabelFrame, textvariable=self.LblInfoBoxTopTxt)
        LblInfoBoxTop.grid(row=0, column=0, sticky='ew')


        self.LblInfoBoxTxt = tk.StringVar()
        self.LblInfoBoxTxt.set('Last Backup: Today')
        LblInfoBox = ttk.Label(BaseLabelFrame, textvariable=self.LblInfoBoxTxt, background='beige')
        LblInfoBox.grid(row=1, column=0, sticky='ew')
        