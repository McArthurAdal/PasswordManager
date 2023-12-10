import tkinter as tk
import tkinter.ttk as ttk
from tkinter.ttk import Style
from upgrade_frame import UpgradeFrame
from main_frame import MainFrame

# Main application window
root = tk.Tk()
root.wm_title("LastPass Clone")
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

style = Style()
tab_font = tk.font.Font(family='Times', name='tabfont', size=9, weight=tk.font.BOLD)

style.theme_use('default')
style.configure('Red.TButton', background='#d32d27')
style.configure('Upgrade.TFrame', background='white')
style.configure('Main.TFrame', background='#f9fafb')
style.configure('TLabel', font='TimesNewRoman', background='white')
style.configure('Caption.TLabel', wraplength=8)
style.configure('TNotebook.Tab', padding=[10], background='#f9fafb')
style.configure('TNotebook', background='#f9fafb')
style.map('TNotebook.Tab', font=[('selected', tab_font)])
style.map('TNotebook.Tab', background=[('active', '#e3e5e7')])

base_frame = ttk.Frame(root)
base_frame.grid()

# assign to variable to display images
mf = MainFrame(base_frame)

separator = ttk.Separator(base_frame, orient='vertical')
separator.grid(row=0, column=1, rowspan=2, sticky='ns')

up = UpgradeFrame(base_frame)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    root.mainloop()
