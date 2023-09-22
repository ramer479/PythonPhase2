import random
from tkinter import *

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Arial"

FILE_PATH = "./data.txt"

# ---------------- Set up an Image UI ---------------- #
# Buttons
window = Tk()
window.config(height=500, width=650)
window.title("Custom Password Manager")
window.config(padx=100, pady=50, bg=YELLOW)

lbl_website = Label(text="Website", bg=YELLOW, font=(FONT_NAME, 13, "bold"))
lbl_website.grid(row=3, column=1)
tbx_website = Entry(width=35, highlightthickness=1)
tbx_website.grid(row=3, column=2, columnspan=5)

lbl_user = Label(text="Username/Email", bg=YELLOW, font=(FONT_NAME, 12, "bold"))
lbl_user.grid(row=4, column=1)
tbx_user = Entry(width=35, highlightthickness=1)
tbx_user.grid(row=4, column=2, columnspan=5)

lbl_pass = Label(text="Password", bg=YELLOW, font=(FONT_NAME, 12, "bold"))
lbl_pass.grid(row=5, column=1)
tbx_pass = Entry(width=16, highlightthickness=1)
tbx_pass.grid(row=5, column=2, columnspan=3)


# ---------------- Generate Password Function ---------------- #
# Generate Password
def generate_password():
    lst = ["A", "E", "I", "O", "U", 1, 2, 3, 4, 5, 6, "#", "$"]
    pss = ""
    for i in range(0, 6):
        pss += str(random.choice(lst))
    tbx_pass.insert(0, pss)


# Copy the password


# ---------------- Add it to the text file ---------------- #
def save_data():
    usr = tbx_user.get()
    pwd = tbx_pass.get()
    website = tbx_website.get()
    data_entry = website + " | " + usr + " | " + pwd
    with open(file=FILE_PATH, mode="w") as data_file:
        data_file.write(data_entry)
        data_file.close()


# Set up a text file
# Copy the Data in specific format


btn_passgen = Button(text="Generate password", height=1, width=14, command=generate_password)
btn_passgen.grid(row=5, column=6, columnspan=2)

btn_add = Button(text="Add", height=1, width=49, command=save_data)
btn_add.grid(row=6, column=1, columnspan=7)
# Text Field
# Image


window.mainloop()
