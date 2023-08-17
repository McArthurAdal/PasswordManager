import tkinter as tk
import tkinter.ttk as ttk
from tkinter import PhotoImage
from tkinter.ttk import Label, Style


# Side frame, upgrade prompt
upgrade_frame = ttk.Frame(width=360, height=600, padding=[50, 100, 50, 96])

# Add text and center
cyl_label = ttk.Label(upgrade_frame, text="Control your digital life", justify='center')
cyl_label.grid()

# Add diamond image and center
diamond_img: PhotoImage = PhotoImage(name='diamond', file='./assets/images/diamond.png')
diamond_label: Label = ttk.Label(upgrade_frame, image=diamond_img, justify='center')
diamond_label.grid()

# Add call to action text
call_action_label = ttk.Label(upgrade_frame,
                              text='Upgrade to LastPass Premium to \n lock in flexibility and convenience.',
                              justify='center')
call_action_label.grid()

# Add access image and center
access_img: PhotoImage = PhotoImage(name='access', file='./assets/images/access.png')
access_label: Label = ttk.Label(upgrade_frame, image=access_img, justify='center')
access_label.grid()

# Add sharing image and center
sharing_img: PhotoImage = PhotoImage(name='sharing', file='./assets/images/sharing.png')
sharing_label: Label = ttk.Label(upgrade_frame, image=sharing_img, justify='center')
sharing_label.grid()

# Add support image and center
support_img: PhotoImage = PhotoImage(name='support', file='./assets/images/support.png')
support_label: Label = ttk.Label(upgrade_frame, image=support_img, justify='center')
support_label.grid()

# Add upgrade button
upgrade_button = ttk.Button(upgrade_frame,
                            text=f'Go premium for only ${3:.2f}/month',)
                            # style='Red.Button')
upgrade_button.grid()

# Add dismiss button
dismiss_button = ttk.Button(upgrade_frame, text=f'Dismiss')
dismiss_button.grid()
