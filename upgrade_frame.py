import tkinter.ttk as ttk
from tkinter import PhotoImage, font
from tkinter.ttk import Label
from PIL import ImageTk, Image


class UpgradeFrame:

    def __init__(self, base_frame):
        # Side frame, upgrade prompt
        self.frame = ttk.Frame(base_frame, width=360, height=600, padding=[12, 12, 12, 0], style='Upgrade.TFrame',)
        self.frame.grid(column=0, row=0)
        self.frame.rowconfigure(0, weight=1)
        self.frame.columnconfigure(0, weight=1)

        # Add text and center
        cyl_label = ttk.Label(self.frame, text="Control your digital life", justify='center', style='TLabel')
        cyl_label.grid(column=0, columnspan=3, row=0)

        # Add diamond image and center
        self.diamond_img: PhotoImage = ImageTk.PhotoImage(image=Image.open(fp='./assets/images/diamond.png'))
        diamond_label: Label = ttk.Label(self.frame, image=self.diamond_img, justify='center', compound='image', wraplength=10)
        diamond_label.grid(column=0, columnspan=3, row=1)

        # Add call to action text
        call_action_label = ttk.Label(self.frame,
                                      text='Upgrade to LastPass Premium to \n lock in flexibility and convenience.',
                                      justify='center')
        call_action_label.grid(column=0, columnspan=3, row=2)

        # Configure caption fonts
        caption_font = font.Font(family='Times', size=12, name='CaptionFont')

        # Add access image and center
        self.access_img: PhotoImage = PhotoImage(file='./assets/images/access.png')
        access_label: Label = ttk.Label(self.frame, image=self.access_img, justify='center', compound='top',
                                        text='Unlimited device access', font='TkIconFont', width=20, wraplength=86)  # font=caption_font)
        access_label.grid(column=0, row=4, pady=15)

        # Add sharing image and center
        self.sharing_img: PhotoImage = PhotoImage(name='sharing', file='./assets/images/sharing.png')
        self.sharing_label: Label = ttk.Label(self.frame, image=self.sharing_img, justify='center', compound='top',
                                              text='One-to-many sharing', font='TkIconFont', width=20, wraplength=59)
        self.sharing_label.grid(column=1, row=4, pady=15)

        # Add support image and center
        self.support_img: PhotoImage = PhotoImage(name='support', file='./assets/images/support.png')
        self.support_label: Label = ttk.Label(self.frame, image=self.support_img, justify='center', compound='top',
                                              text='Direct line to support', font='TkIconFont', width=20, wraplength=86)
        self.support_label.grid(column=2, row=4, pady=15)

        # Add upgrade button
        self.upgrade_button = ttk.Button(self.frame, cursor='hand2', text=f'Go premium for only ${3:.2f}/month',
                                         style='Red.TButton')
        self.upgrade_button.configure(default='normal', padding=0, )
        self.upgrade_button.grid(column=0, columnspan=3, row=5, pady=20, ipadx=20, ipady=10)

        # Add dismiss button
        self.dismiss_button = ttk.Button(self.frame, text=f'Dismiss')
        self.dismiss_button.grid(column=0, columnspan=3, row=6, pady=20)
