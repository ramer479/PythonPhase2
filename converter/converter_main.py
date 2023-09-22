from tkinter import *

window = Tk()
label = Label(text="place in the miles")
label.grid(row=0, column=0)

entry = Entry()
entry.grid(row=0, column=1)

lbl = Label(text="the kms are :")
lbl.grid(row=1, column=0)


def button_clk_action():
    vlu = entry.get()
    kms = 1.60934 * int( vlu)
    lbl2 = Label(text=f"{kms}")
    lbl2.grid(row=1, column=1)


btn = Button(text="click to see", command=button_clk_action)
btn.grid(row=0, column=2)

window.mainloop()
