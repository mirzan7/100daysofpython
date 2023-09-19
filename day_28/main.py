from tkinter import *


PINK = "#E2979C"
RED = "E7305B"
GREEN = "9BDEAC"
FONT_NAME = "Courier"
WORK_MIN = 0.5
SHORT_BREAK_MIN = 0.25
LONG_BREAK_MIN = 0.1
reps = 0
timer = None


def count_down(count):
    second = count % 60
    minute = count // 60
    if second < 10:
        second = f"0{second}"
    canvas.itemconfig(timer_text, text=f"{minute}:{second}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count-1)
    else:
        mark = ""
        for _ in range(reps // 2):
            mark += "*"
        checkpoint.config(text=mark)
        start_timer()


def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break = SHORT_BREAK_MIN * 60
    long_break = LONG_BREAK_MIN * 60
    if reps % 8 == 0:
        count_down(long_break)
        heading.config(text="break")
    elif reps % 2 == 0:
        count_down(short_break)
        heading.config(text="break")
    else:
        count_down(work_sec)
        heading.config(text="work")


def reset_the_clock():
    window.after_cancel(timer)


window = Tk()

window.title("Pomodoro")
window.config(padx=50, pady=50)

heading = Label(text="TIMER", font=(FONT_NAME, 20, "bold"))
heading.grid(column=1, row=0)

canvas = Canvas(width=200, height=225)
timer_text = canvas.create_text(103, 112, text="00:00", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

start_button = Button(text="Start", command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", command=reset_the_clock)
reset_button.grid(column=3, row=2)

checkpoint = check_mark = Label(text="*")
check_mark.grid(column=1, row=3)

window.mainloop()
