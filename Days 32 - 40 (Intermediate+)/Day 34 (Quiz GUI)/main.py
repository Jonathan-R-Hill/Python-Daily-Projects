import tkinter as tk
from data import Questions
from time import sleep

Q = Questions()

score = 0
BG_COL = "black"

window = tk.Tk()
window.title("Quiz (True or False)")
window.config(padx=10, pady=10, bg=BG_COL)


# ---------------------------- Functions -----------------------------#
def true():
    global score
    if Q.question == "End of Quiz. Click again":
        canvas.itemconfig(card_question, text=f"You scored {score}/10")
    elif Q.answer == "True":
        score += 1
        window.configure(bg="green")
        canvas.itemconfig(canvas_score, text=f"Score: {score}")
        sleep(0.5)
        Q.update_question()
        canvas.itemconfig(card_question, text=Q.question)
    else:
        window.configure(bg="red")
        canvas.itemconfig(canvas_score, text=f"Score: {score}")
        sleep(0.5)
        Q.update_question()
        canvas.itemconfig(card_question, text=Q.question)


def false():
    global score
    if Q.answer == "False":
        score += 1
        window.configure(bg="green")
        canvas.itemconfig(canvas_score, text=f"Score: {score}")
        sleep(0.5)
        Q.update_question()
        canvas.itemconfig(card_question, text=Q.question)
    else:
        window.configure(bg="red")
        canvas.itemconfig(canvas_score, text=f"Score: {score}")
        sleep(0.5)
        Q.update_question()
        canvas.itemconfig(card_question, text=Q.question)

    window.configure(bg=BG_COL)


# ------------------------------ UI ------------------------------------#

canvas = tk.Canvas(width=400, height=400,
                   bg=BG_COL, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)
canvas_score = canvas.create_text(340, 20, text=f"Score: {score}", font=("ariel", 20, "italic"), fill="orange")
card_question = canvas.create_text(200, 200, text='blank', font=("ariel", 14, "bold"), fill="white", width=250)
canvas.create_text(200, 50, text="Question:", font=("ariel", 25, "italic"), fill="white")

right_img = tk.PhotoImage(file='images/true.png')
right_button = tk.Button(image=right_img, borderwidth=0,
                         command=true, bg=BG_COL)
right_button.grid(column=1, row=1)

wrong_img = tk.PhotoImage(file='images/false.png')
wrong_button = tk.Button(image=wrong_img, borderwidth=0,
                         command=false, bg=BG_COL)
wrong_button.grid(column=0, row=1)

# -------------------------------- ------------------------------------- #
Q.store_question_ans()
Q.update_question()
canvas.itemconfig(card_question, text=Q.question)

window.mainloop()
