import pandas
import tkinter as tk
import json

BG_COL = "#B1DDC6"

df = pandas.read_csv("data/french_words.csv")
word_index = 0

#------------------------- Windows and Canvas ----------------------#
window = tk.Tk()
window.title("PW Manager")
window.config(padx = 20, pady = 10, bg = BG_COL)


#------------------------------ Functions -----------------------#
def flip_card():

    if word_label['text'] == df.iloc[word_index][0]:  # french word
        word_label.config(text= df.iloc[word_index][1]) # english word

def right():
    global word_index
    save("right.json")
    word_index += 1
    word_label.config(text= df.iloc[word_index][0])
    
def wrong():
    global word_index
    save("wrong.json")
    word_index += 1
    word_label.config(text= df.iloc[word_index][0])
    
def save(place):
    french = df.iloc[word_index][0]
    english = df.iloc[word_index][1]
    new_data = {f"Word{word_index}":{
            "french": french,
            "english": english
            }
        }
    try:
        with open(place,'r') as file:
            data = json.load(file) # read old data
                
    except FileNotFoundError:
        with open(place, 'w') as file:
            json.dump(new_data, file, indent = 4)
    else:
        data.update(new_data) # use old data with new  
             
        with open(place,'w') as file:

            json.dump(data, file, indent = 4)
    finally:
        pass


#-------------------------------- UI --------------------------------#
flip_button = tk.Button(text = "Flip Card",
                        font= ("Arial",8), width = 13,
                        command = flip_card, bg = BG_COL)

right_img= tk.PhotoImage(file='images/right.png')
right_button = tk.Button(image = right_img, borderwidth=0,
                        command = right, bg = BG_COL)

wrong_img= tk.PhotoImage(file='images/wrong.png')
wrong_button = tk.Button(image = wrong_img, borderwidth=0,
                        command = wrong, bg = BG_COL)

word_label = tk.Label(font = ("arial", 20, "bold"), bg = BG_COL)
word_label.config(text = df.iloc[word_index][0])

right_button.grid(column= 2, row= 1)
wrong_button.grid(column= 0, row= 1)
flip_button.grid(column= 1, row= 1)

word_label.grid(column= 1, row= 0)


window.mainloop()