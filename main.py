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
style.theme_use('default')
style.configure('Red.TButton', background='#d32d27')
style.configure('TFrame', background='white')
style.configure('TLabel', font='TimesNewRoman', background='white')

base_frame = ttk.Frame(root, width=735, height=600, borderwidth=10)
base_frame.grid()

# assign to variable to display images
mf = MainFrame(base_frame)

separator = ttk.Separator(base_frame, orient='vertical')
separator.grid(row=0, column=1, rowspan=2, sticky='ns')

up = UpgradeFrame(base_frame)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    root.mainloop()
