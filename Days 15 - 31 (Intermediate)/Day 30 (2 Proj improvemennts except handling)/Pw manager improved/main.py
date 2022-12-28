import tkinter as tk
from tkinter import messagebox
from random import choice, shuffle
import pyperclip
import json

email_add = "jonny@test.com"

# Window
window = tk.Tk()
window.title("PW Manager")
window.config(padx = 20, pady = 10, bg = "white")

# Canvas   logo
canvas = tk.Canvas(width = 200, height = 200,
                   bg = "white",highlightthickness = 0)
logo = tk.PhotoImage(file = "logo.png")
canvas.create_image(100, 100, image = logo)

#----------------------------- Functions ------------------------------#
def password_gen():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    pw = []
    for _ in range(6):
        num = choice(letters)
        pw.append(num)

    for _ in range(2):
        num = choice(symbols)
        pw.append(num)

    for _ in range(4):
        num = choice(numbers)
        pw.append(num)

    shuffle(pw)

    password = ''.join(pw)
    pyperclip.copy(password)
    
    password_input.delete(0, tk.END)
    password_input.insert(tk.END, f"{password}")

def save():
    site = website_input.get()
    email = email_input.get()
    pw = password_input.get()
    new_data = {
        site: {
            "email": email,
            "password": pw
            }
        }
    
    if len(site) == 0 or len(email) == 0 or len(pw) == 0:
        messagebox.showwarning(title = 'Missing Entry',
                        message = "Please check and fill all of the data.")

    else: 
        try:
            with open('data.json','r') as file:
                data = json.load(file) # read old data
                
        except FileNotFoundError:
            with open("data.json", 'w') as file:
                json.dump(new_data, file, indent = 4)
        else:
            data.update(new_data) # use old data with new  
             
            with open('data.json','w') as file:

                json.dump(data, file, indent = 4)
        finally:
            website_input.delete(0, tk.END)
            password_input.delete(0, tk.END)
        

def search():
    site = website_input.get()
    try:
        with open("data.json", 'r') as file:
            data = json.load(file)
        messagebox.showinfo(title = str(site), 
                        message = f'Email: {data[site]["email"]}\nPassword: {data[site]["password"]}')
    except KeyError:
        messagebox.showinfo(title = str(site), 
                        message = f'No website data found')
        
# ------------------------------- UI -------------------------------- #
website_label = tk.Label(text = "Website: ", bg = "white")
email = tk.Label(text = "Email/Username: ", bg = "white")
password = tk.Label(text = "Password", bg = "white")

generate_button = tk.Button(text = "Generate",
                            font= ("Arial",8), width = 13,
                            command = password_gen, bg = "white")
add_button = tk.Button(text = "Add", command = save, width= 40, bg = "white")
search_button = tk.Button(text = "search", command = search, 
                          font= ("Arial",8), width = 13, bg= "white")

website_input = tk.Entry(width= 35, bg = "white")
email_input = tk.Entry(width = 50, bg = "white")
password_input = tk.Entry(width = 35, bg = "white")

#------------------------------ Layout ---------------------------#
website_label.grid(column= 0, row= 1)
email.grid(column= 0, row= 2)
password.grid(column= 0, row= 3)

website_input.grid(column= 1, row= 1,)
email_input.grid(column= 1, row= 2, columnspan=2)
password_input.grid(column= 1, row= 3)

search_button.grid(column= 2, row= 1)
generate_button.grid(column= 2, row= 3)
add_button.grid(column= 1, row= 4, columnspan=2)
canvas.grid(column= 1, row= 0)

website_input.focus()
email_input.insert(tk.END, email_add)



# Stay at the end
window.mainloop()