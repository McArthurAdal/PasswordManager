import tkinter as tk
import tkinter.ttk as ttk
from tkinter import PhotoImage
from tkinter.ttk import Label, Style
from main import root

main_frame = ttk.Frame(root, width=360, height=600, padding=[50, 100, 50, 96])

searchText = tk.StringVar()
entry = ttk.Entry(main_frame, textvariable=searchText)



