import tkinter as tk

# create window
window = tk.Tk()
window.minsize(width = 200, height = 100)
window.title("Miles to Km")
window.config(padx= 10, pady= 10) 


def miles_to_kilo():
    miles = miles_input.get()
    Km = round(int(miles) * 1.609, 2)
    answer_text.config(text = f"{Km}")


calculate_but = tk.Button(text= "Calculate", command = miles_to_kilo)
answer_text = tk.Label(text = "")

equal_text = tk.Label(text= "is equal to:") 

miles_input = tk.Entry(width = 7)

km_text = tk.Label(text= "Km")
mile_text = tk.Label(text= "Miles")

# place widgets
miles_input.grid(column= 1, row= 0)
mile_text.grid(column= 2, row= 0)

equal_text.grid(column= 0, row= 1)
answer_text.grid(column= 1, row= 1)
km_text.grid(column= 2, row = 1)

calculate_but.grid(column= 1, row= 2)



window.mainloop()