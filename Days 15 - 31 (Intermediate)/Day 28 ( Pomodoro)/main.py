import tkinter as tk
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
font = (FONT_NAME, 32, "bold")
tick = "✅"
timer = None
# ---------------------------- UI SETUP ------------------------------- #
# Window
window = tk.Tk()
window.title("Timer")
window.config(padx = 30, pady = 20, bg = YELLOW, width = 350, height = 350)

# Canvas   tomato
canvas = tk.Canvas(width = 220, height = 240,
                   bg = YELLOW,highlightthickness = 0)
tom_pic = tk.PhotoImage(file = "tomato.png")
canvas.create_image(110, 120, image = tom_pic)
timer_txt = canvas.create_text(110, 140, text = "00:00", fill = "white", font = font)
canvas.grid(column= 1, row = 1)
reps = 0

#----------------------------Functions---------------------------------#
def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        title_label.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        title_label.config(text="Break", fg=PINK)
    else:
        count_down(work_sec)
        title_label.config(text="Work", fg=GREEN)
    
    
def reset_timer():
    global reps
    global timer
    reps = 0
    
    window.after_cancel(timer)
    check_marks.config(text = '')
    canvas.itemconfig(timer_txt, text= f"00:00")
    title_label.config(text = "Timer", fg = GREEN)
    
def count_down(number):
    global timer
    min = math.floor(number / 60)
    sec = number % 60
    if sec < 10:
        sec = f"0{sec}"
        
    canvas.itemconfig(timer_txt, text= f"{min}:{sec}")
    
    if number > 0:
        timer = window.after(1000, count_down, number - 1)
    else:
        start_timer()
        if reps % 2 == 0:
            marks = math.floor(reps / 2) # Work sessions
            new_ticks = tick * marks
            check_marks.config(text = new_ticks)
    
    
 #----------------------------- Labels ----------------------------------#
title_label = tk.Label(text = "Timer", font = font,
                 bg = YELLOW, highlightthickness= 0,
                 fg = GREEN)
title_label.grid(column = 1, row = 0)

check_marks = tk.Label(fg=GREEN, bg=YELLOW)
check_marks.grid(column=1, row=3)


# ---------------------------- Buttons----------------------------------#
button_start = tk.Button(text= "Start", 
                         highlightthickness= 0, command= start_timer)

button_start.grid(column = 0, row = 3)

button_reset = tk.Button(text = "Reset", 
                         highlightthickness= 0, command= reset_timer)

button_reset.grid(column= 3, row = 3)


# ----------------- always at bottom----------------------#
window.mainloop()