import tkinter as tk
from tkinter import ttk
import mainframemethods as mfm

class MainWindow(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry('800x600')
        self.title('Backup System')
        self.columnconfigure(0, weight=2)
        # self.rowconfigure(0, weight=5)
        # self.rowconfigure(1, weight=1)
        
        self.frames_dic = {}

        self.EditFrame1 = EditFrame(self, self)
        self.EditFrame1.grid(row=0, column=0, sticky='nsew', padx=10, pady=20)

        self.BaseFrame1 = BaseFrame(self, self)
        self.BaseFrame1.grid(row=0, column=0, sticky='nsew', padx=10, pady=20)

        self.frames_dic[EditFrame] = self.EditFrame1
        self.frames_dic[BaseFrame] = self.BaseFrame1
        
    def switch_topframe(self, container):
        frame = self.frames_dic[container]
        frame.tkraise()
        
class BaseFrame(mfm.BaseFrameMethods):
    def __init__(self,container, controller, **kwargs):
        super().__init__(container, **kwargs)
        self.configure(relief='sunken',border=1)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)
        # self.grid(sticky='ew', padx=10, pady=20)
        
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
        cmdEdit = ttk.Button(BaseButtonFrame, textvariable=self.cmdEditTxt, command=lambda: controller.switch_topframe(EditFrame))
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
        
        
class EditFrame(ttk.Frame):
    def __init__(self, container, controller, **kwargs):
        super().__init__(container, **kwargs)
        self.configure(relief='sunken',border=1)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)
        # self.grid(sticky='ew', padx=10, pady=20)
        
        cmd_add_files = ttk.Button(self, text='Add Files')
        cmd_add_files.grid(row=0, column=0)
        
        cmd_remove_files = ttk.Button(self, text='Remove Files')
        cmd_remove_files.grid(row=0, column=1)

        cmd_add_folders = ttk.Button(self, text='Add Folders')
        cmd_add_folders.grid(row=1, column=0)
        
        cmd_remove_folders = ttk.Button(self, text='Remove Folders')
        cmd_remove_folders.grid(row=1, column=1)
        
        cmd_edit_name = ttk.Button(self, text='Edit Name')
        cmd_edit_name.grid(row=2, column=0)
        
        cmd_cancel = ttk.Button(self, text='Cancel', command=lambda: controller.switch_topframe(BaseFrame))
        cmd_cancel.grid(row=10,column=3)
        
        cmd_apply = ttk.Button(self, text='Apply')
        cmd_apply.grid(row=10,column=4)
        
        cmd_ok = ttk.Button(self, text='Ok')
        cmd_ok.grid(row=10,column=5)
        
        cmd_edit_backuplocation = ttk.Button(self, text='Edit Backup-Location')
        cmd_edit_backuplocation.grid(row=0,column=3)
        
        var_info = tk.StringVar()
        lbl_info = ttk.Label(self, textvariable=var_info, text='Empty Var')
        lbl_info.grid(row=1, column=3)