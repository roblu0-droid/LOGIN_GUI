

import tkinter as tk
from tkinter import messagebox
import os
from PIL import Image, ImageTk

# LOGIN FUNCTION
def login():
    username = username_entry.get()
    password = password_entry.get()

    if username == "admin" and password == "12345":
        messagebox.showinfo(
            "LOGIN SUCCESSFUL!",
            "Welcome Admin!"
        )
    else:
        messagebox.showerror(
            "LOGIN FAILED!",
            "Invalid Username and Password!"
        )



# BUTTONS
def button_enter(event):
    login_button.config(
        bg="#FF35B8",
        fg="white"
    )


def button_leave(event):
    login_button.config(
        bg="#7B2CFF",
        fg="white"
    )



# MAIN WINDOW
root = tk.Tk()
root.title("USER LOGIN")
root.geometry("500x600")
root.resizable(False, False)


# KDA THEME
DARK = "#130B24"
PURPLE = "#7B2CFF"
PINK = "#FF35B8"
CYAN = "#00E5FF"
WHITE = "#F5EFFF"



# BG
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
img_path = os.path.join(BASE_DIR, "KDA_BG.JPG")

img = Image.open(img_path)
img = img.resize((500, 600), Image.Resampling.LANCZOS)

bg_image = ImageTk.PhotoImage(img)

background = tk.Label(root, image=bg_image)
background.place(x=0, y=0, relwidth=1, relheight=1)



# LOGIN PANEL
panel = tk.Frame(
    root,
    bg=DARK,
    highlightbackground=PURPLE,
    highlightthickness=2
)

panel.place(
    relx=0.5,
    rely=0.5,
    anchor="center",
    width=370,
    height=440
)



# TITLE
title_label = tk.Label(
    panel,
    text="USER",
    font=("Arial", 32, "bold"),
    bg=DARK,
    fg=PINK
)
title_label.pack(pady=(20, 0))


subtitle_label = tk.Label(
    panel,
    text="LOGIN",
    font=("Arial", 11, "bold"),
    bg=DARK,
    fg=CYAN
)
subtitle_label.pack(pady=(0, 15))


# DIVIDER
divider = tk.Frame(
    panel,
    bg=PURPLE,
    height=2,
    width=250
)
divider.pack(pady=5)



# USERNAME LABEL
username_label = tk.Label(
    panel,
    text="USERNAME",
    font=("Arial", 11, "bold"),
    bg=DARK,
    fg=CYAN
)
username_label.pack(anchor="w", padx=55, pady=(20, 5))


# USERNAME ENTRY
username_entry = tk.Entry(
    panel,
    font=("Arial", 13),
    width=25,
    bg="#241638",
    fg=WHITE,
    insertbackground=CYAN,
    relief="flat",
    highlightthickness=1,
    highlightbackground=PURPLE,
    highlightcolor=CYAN
)
username_entry.pack(ipady=9, padx=50)



# PASSWORD LABEL
password_label = tk.Label(
    panel,
    text="PASSWORD",
    font=("Arial", 11, "bold"),
    bg=DARK,
    fg=CYAN
)
password_label.pack(anchor="w", padx=55, pady=(20, 5))


# PASSWORD ENTRY
password_entry = tk.Entry(
    panel,
    font=("Arial", 13),
    width=25,
    show="*",
    bg="#241638",
    fg=WHITE,
    insertbackground=CYAN,
    relief="flat",
    highlightthickness=1,
    highlightbackground=PURPLE,
    highlightcolor=CYAN
)
password_entry.pack(ipady=9, padx=50)


# LOGIN BUTTON
login_button = tk.Button(
    panel,
    text="L O G   I N",
    font=("Arial", 12, "bold"),
    bg=PURPLE,
    fg=WHITE,
    activebackground=PINK,
    activeforeground=WHITE,
    width=22,
    height=2,
    relief="flat",
    cursor="hand2",
    command=login
)

login_button.pack(pady=30)




# RUN APPLICATION
root.mainloop()
