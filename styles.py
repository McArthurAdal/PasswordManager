from tkinter import ttk


# class MyStyle(ttk.Style):
#     def __init__(self):
style = ttk.Style()
style.theme_use('classic')
style.configure('Red.TButton', background='#d32d27')
style.configure('TFrame', background='white')
style.configure('TLabel', font='TimesNewRoman', background='white')
