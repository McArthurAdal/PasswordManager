import tkinter as tk
from tkinter import ttk


class PlaceholderEntry(ttk.Entry):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)  # modify, not override
        self.configure(foreground='grey')
        self.bind("<FocusIn>", self.foc_in)
        self.bind("<FocusOut>", self.foc_out)

    def foc_in(self, *args):
        # self.configure(foreground='grey')
        if self.get() == 'Search' or self.get() is None:
            self.delete(0, 'end')
            self.configure(foreground='black')

    def foc_out(self, *args):
        if self.get() is None:
            self.insert(0, "Search")
            self.configure(foreground='grey')
