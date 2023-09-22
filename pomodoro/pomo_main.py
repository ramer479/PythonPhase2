from math import ceil, floor
from tkinter import *
import time

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 2
SHORT_BREAK_MIN = 1
LONG_BREAK_MIN = 1
reps = 0
tim = None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global reps
    reps = 0
    window.after_cancel(tim)
    canvas.itemconfig(timer_text, text="00:00")
    lbl_timer.config(text="Timer")
    lbl_check.config(text="")

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def run_timer(tm_ct):
    global tim
    min_ct = floor((tm_ct / 60))
    sec_ct = tm_ct % 60
    if sec_ct < 10:
        sec_ct = f"0{sec_ct}"
    canvas.itemconfig(timer_text, text=f"{min_ct}:{sec_ct}")
    if tm_ct > 0:
        tim = window.after(1000, run_timer,tm_ct-1)
        tim
    elif tm_ct == 0:
        start_timer()
    else:
        print("reset the timer")


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def start_timer():
    timer_name = ""
    count_time = 0
    global reps
    reps += 1

    if reps % 8 == 0:
        count_time = LONG_BREAK_MIN * 60
        timer_name = "Long Break Timer"

    elif reps % 2 == 0:
        count_time = SHORT_BREAK_MIN * 60
        timer_name = "Short Break Timer"
    elif reps % 2 == 1:
        count_time = WORK_MIN * 60
        timer_name = "Work Timer"
        if reps % 8 == 1:
            lbl_check.config(text="✔", fg = GREEN, font=(FONT_NAME,20,"bold"))
        elif reps % 8 == 3:
            lbl_check.config(text="✔✔", fg = GREEN, font=(FONT_NAME,20,"bold"))
        elif reps % 8 == 5:
            lbl_check.config(text="✔✔✔", fg = GREEN, font=(FONT_NAME,20,"bold"))
        elif reps % 8 == 7:
            lbl_check.config(text="✔✔✔✔", fg = GREEN, font=(FONT_NAME,20,"bold"))

    lbl_timer.config(text=timer_name)
    run_timer(count_time)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

lbl_timer = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 45, "italic"))
lbl_timer.grid(row=1, column=2)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
check_text = "✔"
lbl_check = Label(text=check_text)
lbl_check.grid(row=3, column=2)
canvas.grid(row=2, column=2)



btn_start = Button(text="start", command = start_timer)
btn_start.grid(row=4, column=1)

btn_reset = Button(text="reset", command=reset_timer)
btn_reset.grid(row=4, column=4)





window.mainloop()
