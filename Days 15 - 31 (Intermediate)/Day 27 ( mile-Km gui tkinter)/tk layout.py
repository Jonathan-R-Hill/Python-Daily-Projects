from tkinter import *

window = Tk()
window.minsize(width = 500, height = 300)
window.title("First GUI")
window.config(padx= 20, pady= 20) 
# space from edge or widget cando with widgets aswell

def button_clicked():
    mylabel.config(text = input.get())


# Label
mylabel = Label(text= "???", font= ("Arial", 20, "italic")) # create
mylabel.config(text = "???")
mylabel.grid(column=0, row=0)

# button 1
button1 = Button(text= "Click me", command = button_clicked)
button1.grid(column= 1, row= 1)

# button 2
button2 = Button(text= "New button")
button2.grid(column=2, row= 0)

# Entry
input = Entry(width = 10)
input.grid(column=3, row= 2)



window.mainloop()