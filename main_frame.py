import tkinter as tk
import tkinter.ttk as ttk
from tkinter import PhotoImage
from tkinter.ttk import Label, Style


class MainFrame:
    def __init__(self, base_frame):
        # Main frame
        main_frame = ttk.Frame(base_frame, width=360, height=600, padding=[50, 100, 50, 96])
        main_frame.grid(column=1, row=0)
        self.searchText = tk.StringVar()
        entry = ttk.Entry(main_frame, textvariable=self.searchText)
        entry.grid()
