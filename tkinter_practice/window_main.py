import tkinter as tk
from tkinter import *

window = tk.Tk()
window.title("Raghuram Workshop")
naam = ""
entry = tk.Entry()
entry.grid(row=3,column=4)

label = tk.Label(text=f"What is your name? Name is : {naam}")
label.grid(row=0,column=0)


def action_button_click():
    print("Come onnn !")
    var = entry.get()
    print(var)
    label.config(text=f"{var}")


button = tk.Button(text="Click to Load", command=action_button_click)
button.grid(row=2,column=2)

button = tk.Button(text="New Button")
button.grid(row=1,column=3)

window.mainloop()
