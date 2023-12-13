import tkinter as tk
import tkinter.ttk as ttk
from styles import MyStyles
from upgrade_frame import UpgradeFrame
from main_frame import MainFrame

# Main application window
root = tk.Tk()
root.wm_title("LastPass Clone")
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

MyStyles()

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
