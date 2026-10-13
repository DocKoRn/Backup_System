import tkinter as tk
from tkinter import ttk

class BaseFrameMethods(ttk.Frame):
    def __init__(self, container, **kwargs):
        super().__init__(container)
    
    def handle_cmdRemove(self):
        print('overwritten this - handle_cmdRemove')