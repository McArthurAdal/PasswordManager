from tkinter import ttk
import tkinter as tk


class MyStyles(ttk.Style):
    def __init__(self):
        super().__init__()
        tab_font = tk.font.Font(family='Times', name='tabfont', size=9, weight=tk.font.BOLD)

        self.theme_use('default')
        self.configure('Red.TButton', background='#d32d27')
        self.configure('Plus.TButton', background='blue', bordercolor  ='red')
        self.configure('Upgrade.TFrame', background='white')
        self.configure('Main.TFrame', background='#f9fafb')
        self.configure('TLabel', font='TimesNewRoman', background='white')
        self.configure('Caption.TLabel', wraplength=8)
        self.configure('TNotebook.Tab', padding=[10], background='#f9fafb')
        self.configure('TNotebook', background='#f9fafb')
        self.map('TNotebook.Tab', font=[('selected', tab_font)])
        self.map('TNotebook.Tab', background=[('active', '#e3e5e7')])
