from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = .2
SHORT_BREAK_MIN = .5
LONG_BREAK_MIN = 1
CHECKMARK = "✔"
checkmark_string = ""
REPS = 0 
TIMER = 0

def reset():
    window.after_cancel(TIMER)
    global checkmark_string, REPS
    title_label.config(text="Pomodoro")
    canvas.itemconfig(timer_text,text="00:00")
    check_label.config(text="")
    checkmark_string = ""
    REPS = 0

def get_time_string(count):
    count_min = math.floor(count/60)
    count_sec = int(count % 60)
    if count_sec == 0:
        count_sec = "00"
    elif count_sec < 10: 
        count_sec = f"0{count_sec}"
    return f"{count_min}:{count_sec}"   

def adjust_time_to_sec(min):
    return min * 60

def time_loop():
    global REPS
    REPS += 1
    if REPS % 8 == 0:
        count_down(count=adjust_time_to_sec(LONG_BREAK_MIN))
        title_label.config(text="Long Break")
    elif REPS % 2 == 0:
        count_down(count=adjust_time_to_sec(SHORT_BREAK_MIN))
        title_label.config(text="Short Break")
    else:
        count_down(count=adjust_time_to_sec(WORK_MIN))
        title_label.config(text="Work")
    

def count_down(count,):
    global checkmark_string, TIMER
    time_str = get_time_string(count=count)
    if count >= 0:
        TIMER = window.after(1000,count_down,count-1)
        canvas.itemconfig(timer_text, text=time_str)
    else:
        checkmark_string = checkmark_string + CHECKMARK
        check_label.config(text=checkmark_string)
        time_loop()

window = Tk()
window.title("Pomodoro Counter")
window.config(padx=95, pady=50)
TOMATO_PNG = PhotoImage(file="OHDC_28\\tomato.png")

check_label = Label(text="")
check_label.grid(column=1,row=6)

title_label = Label(text="",font=(FONT_NAME, 12,"bold"))
title_label.grid(column=2,row=0)

canvas = Canvas(width=200,height=224,highlightthickness=0)
canvas.create_image(100,112,image=TOMATO_PNG)
timer_text = canvas.create_text(102,130, text="", fill="white",font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1,row=4)

start_button = Button(text="Start", command=time_loop)
start_button.grid(column=0,row=5)

reset_button = Button(text="Reset", command=reset)
reset_button.grid(column=3,row=5)

window.mainloop()