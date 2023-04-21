import time
from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
GREEN = "#3CCF4E"
WHITE = "#CFD2CF"
PINK = "#FA9494"
BLACK = "#2C3333"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
mark = ""
timer = None
# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global timer, mark, reps
    window.after_cancel(timer)
    mark = ""
    text_label.config(text="Timer", fg = fg)
    canvas.itemconfig(timer_text, text="00:00")
    reps = 0
# ---------------------------- TIMER MECHANISM ------------------------------- # 


def amount():
    global reps, mark
    reps += 1
    if reps % 2 != 0:
        secs = WORK_MIN * 60
        count_down(secs)
        text_label.config(text="Work", fg = GREEN)
    elif reps % 2 == 0 and reps % 8 != 0:
        secs = SHORT_BREAK_MIN * 60
        count_down(secs)
        text_label.config(text="Break", fg = "gold")
    elif reps % 8 == 0:
        secs = LONG_BREAK_MIN * 60
        count_down(secs)
        text_label.config(text="Break", fg="red")
        mark += "✔"
        check_mark.config(text=mark)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def count_down(total_sec):
    global timer
    minutes = total_sec // 60
    seconds = total_sec % 60
    if seconds < 10:
        seconds = "0" + str(seconds)

    if minutes < 10:
        minutes = "0" + str(minutes)
    canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")
    if total_sec > 0:
        timer = window.after(1000, count_down, total_sec - 1)
    else:
        amount()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(pady=100, padx=100, bg=PINK)
canvas = Canvas(width=210, height=224, bg=PINK, highlightthickness=0)

fg = BLACK
text_label = Label(text="Timer", fg=fg, bg=PINK, font=(FONT_NAME, 30, "bold"))
text_label.grid(column=1, row=0)
image = PhotoImage(file="tomato.png")
canvas.create_image(105, 112, image=image)
timer_text = canvas.create_text(108, 130, text="00:00", fill="#E8F9FD", font=(FONT_NAME, 28, "bold"))
canvas.grid(column=1, row=1)

start_button = Button(text="Start", width=4, highlightthickness=0, command=amount)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", width=4, highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)

check_mark = Label(padx=10, pady=10, fg=GREEN, bg=PINK, text="", font=50)
check_mark.grid(column=1, row=2)

window.mainloop()
