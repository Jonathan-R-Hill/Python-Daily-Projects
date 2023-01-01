import pandas
import tkinter as tk
import json
import random

BG_COL = "#B1DDC6"

try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")
current_word = {}

#------------------------- Windows and Canvas ----------------------#
window = tk.Tk()
window.title("Flash Card")
window.config(padx = 50, pady = 50, bg = BG_COL)


#------------------------------ Functions -----------------------#
def is_known():
    to_learn.remove(current_word)
    print(len(to_learn))
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    next_card()

def next_card():
    global current_word, flip_timer
    window.after_cancel(flip_timer)
    current_word = random.choice(to_learn)

    french = current_word["French"]
    canvas.itemconfig(card_title, text= "French", fill = "black")
    canvas.itemconfig(card_word, text= french, fill = "black")
    canvas.itemconfig(card_background, image= card_front)

    flip_timer = window.after(5000, change_card)

def change_card():
    english = current_word["English"]
    canvas.itemconfig(card_title, text= "English", fill = "white")
    canvas.itemconfig(card_word, text= english, fill = "white")
    canvas.itemconfig(card_background, image= card_back)

    window.after_cancel(flip_timer)

flip_timer = window.after(5000, func = change_card)
#-------------------------------- UI --------------------------------#
canvas = tk.Canvas(width = 800, height = 526,
                   bg = BG_COL,highlightthickness = 0)
card_front = tk.PhotoImage(file = "images/card_front.png")
card_back = tk.PhotoImage(file = "images/card_back.png")
card_background = canvas.create_image(400, 263, image = card_front)
canvas.grid(row= 0, column= 0, columnspan= 2)
card_title = canvas.create_text(400, 150, text = "", font= ("ariel", 30))
card_word = canvas.create_text(400, 263, text = "", font= ("ariel", 40, "bold"))


right_img= tk.PhotoImage(file='images/right.png')
right_button = tk.Button(image = right_img, borderwidth=0,
                        command = is_known, bg = BG_COL)
right_button.grid(column=1, row= 1)

wrong_img= tk.PhotoImage(file='images/wrong.png')
wrong_button = tk.Button(image = wrong_img, borderwidth=0,
                        command = next_card, bg = BG_COL)
wrong_button.grid(column= 0, row= 1)



next_card()



window.mainloop()