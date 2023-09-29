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
style.theme_use('classic')
style.configure('Red.TButton', background='#d32d27')
style.configure('TFrame', background='white')
style.configure('TLabel', font='TimesNewRoman', background='white')

base_frame = ttk.Frame(root)
base_frame.grid()

MainFrame(base_frame)
UpgradeFrame(base_frame)



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    root.mainloop()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
