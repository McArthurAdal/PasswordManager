import tkinter as tk
import tkinter.ttk as ttk
from tkinter import PhotoImage


class MainFrame:
    def __init__(self, base_frame):
        # TODO: Manage whitespace, padding, and margins
        # Main frame

        self.main_frame = ttk.Frame(base_frame, style='Main.TFrame',width=375, height=600, padding=[12, 12, 12, 12])
        self.main_frame.grid(column=2, row=0, sticky='nswe')

        self.searchText = tk.StringVar()
        entry = ttk.Entry(self.main_frame, textvariable=self.searchText, width=30)
        entry.grid(row=0, column=0, sticky='nws')

        # TODO: Separate vault button and plus button
        self.vault_arrow = PhotoImage(name='vault_arrow', file='assets/images/vault_arrows.png')
        vault_button = ttk.Button(self.main_frame, text='Vault', style='Red.TButton',
                                  image=['vault_arrow'],
                                  width=8,
                                  compound='right')
        vault_button.grid(row=0, column=1, sticky='nw', padx=20, )

        # TODO: Remove plus button background
        self.plus_icon = PhotoImage(name='plus_icon', file='./assets/images/plus_png.png')
        plus_label = ttk.Button(master=self.main_frame, image=['plus_icon'])
        plus_label.grid(row=0, column=2, sticky='ne')

        # TODO: Figure out why separators are small
        separator = ttk.Separator(self.main_frame, orient='horizontal')
        separator.grid(row=1, columnspan=2, sticky='we', pady=20)

        self.n = ttk.Notebook(self.main_frame)
        f1 = ttk.Frame(self.n)  # first page, which would get widgets gridded into it
        f2 = ttk.Frame(self.n)  # second page
        f3 = ttk.Frame(self.n)  # second page
        f4 = ttk.Frame(self.n)  # second page
        self.n.add(f1, text='All Relevant')
        self.n.add(f2, text='All Items')
        self.n.add(f3, text='Favorites')
        self.n.add(f4, text='Recent')
        self.n.grid(row=2, columnspan=2, sticky='we')
