import tkinter as tk
import tkinter.ttk as ttk
from tkinter import PhotoImage
from tkinter.ttk import Label, Style


class UpgradeFrame:
    def __init__(self, base_frame):
        # Side frame, upgrade prompt
        upgrade_frame = ttk.Frame(base_frame, width=360, height=600, padding=[50, 100, 50, 96], style='TFrame')
        upgrade_frame.grid(column=0, row=0)
        upgrade_frame.rowconfigure(0, weight=1)
        upgrade_frame.columnconfigure(0, weight=1)

        # Add text and center
        cyl_label = ttk.Label(upgrade_frame, text="Control your digital life", justify='center', style='TLabel')
        cyl_label.grid(column=0, columnspan=3, row=0)

        # Add diamond image and center
        diamond_img: PhotoImage = PhotoImage(name='diamond', file='./assets/images/diamond.png')
        diamond_label: Label = ttk.Label(upgrade_frame, image=diamond_img, justify='center')
        diamond_label.grid(column=0, columnspan=3, row=1)

        # Add call to action text
        call_action_label = ttk.Label(upgrade_frame,
                                      text='Upgrade to LastPass Premium to \n lock in flexibility and convenience.',
                                      justify='center')
        call_action_label.grid(column=0, columnspan=3, row=2)

        # Add access image and center
        access_img: PhotoImage = PhotoImage(name='access', file='./assets/images/access.png')
        access_label: Label = ttk.Label(upgrade_frame, image=access_img, justify='center')
        access_label.grid(column=0, row=4)

        # Add sharing image and center
        sharing_img: PhotoImage = PhotoImage(name='sharing', file='./assets/images/sharing.png')
        sharing_label: Label = ttk.Label(upgrade_frame, image=sharing_img, justify='center')
        sharing_label.grid(column=1, row=4)

        # Add support image and center
        support_img: PhotoImage = PhotoImage(name='support', file='./assets/images/support.png')
        support_label: Label = ttk.Label(upgrade_frame, image=support_img, justify='center')
        support_label.grid(column=2, row=4)

        # Add upgrade button
        upgrade_button = ttk.Button(upgrade_frame,
                                    cursor='hand2',
                                    text=f'Go premium for only ${3:.2f}/month',
                                    style='Red.TButton')
        upgrade_button.configure(default='normal', padding=0)
        upgrade_button.grid(column=0, columnspan=3, row=5)

        # Add dismiss button
        dismiss_button = ttk.Button(upgrade_frame, text=f'Dismiss')
        dismiss_button.grid(column=0, columnspan=3, row=6)
