from tkinter import *

window = Tk()
window.minsize(width = 500, height = 300)
window.title("First GUI")

# Label
mylabel = Label(text= "???", font= ("Arial", 20, "italic")) # create
mylabel.config(text = "???")
mylabel.pack(side= "left") # put on screen

# button
def button_clicked():
    mylabel.config(text = input.get())
    
button = Button(text= "Click me", command = button_clicked)
button.pack()

# Entry

input = Entry(width = 10)
input.pack()

# Text box
text = Text(height= 5, width = 20)
text.focus() # cursor stats in that box
text.insert(END, "test") # Enter starting text
print(text.get("1.0", END))  # 1.0 first line char 0
text.pack()

# Spinbox (size thingy)
def spinbox_used():
    print(spinbox.get()) # gets the current val in spinbox
spinbox = Spinbox(from_= 0, to= 10, width = 5, command= spinbox_used)
spinbox.pack()

#scale
# called with current scale value
def Scale_used(value):
    print(value)
scale = Scale(from_= 0, to= 100, command= Scale_used)
scale.pack()

#check button
def checkbutton_used():
    # prints 1 if checked 0 if not
    print(checked_state.get())
checked_state = IntVar() # class to track val of checkbox
checkbutton = Checkbutton(text= "Is On?", 
                          variable=checked_state, 
                          command=checkbutton_used)
checked_state.get()
checkbutton.pack()


# Radio Button
def radio_used():
    print(radio_state.get())
radio_state = IntVar()
radiobutton1 = Radiobutton(text= "Option 1", value = 1, 
                           variable=radio_state, command=radio_used)
radiobutton2 = Radiobutton(text= "Option 2", value = 2, 
                           variable=radio_state, command=radio_used)
radiobutton1.pack()
radiobutton2.pack()

# list box
def listbox_used(event):
    #gets current selection
    print(listbox.get(listbox.curselection()))
    
listbox = Listbox(height= 4)
fruits = ["Apple", "Pear", "Orange", "Banana"]
for item in fruits:
    listbox.insert(fruits.index(item), item)
listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.pack()



window.mainloop()