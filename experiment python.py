

import tkinter as tk

root = tk.Tk()
root.title("Climbing Score Calculator")
root.configure(background = "white")                                                                                    #figured out how to make ceritan background color from this website: https://stackoverflow.com/questions/2744795/background-color-for-tk-in-python
introduction = tk.Label(text = "Welcome to the bouldering competition points cointer!", fg="purple", bg="white")


climb_input = tk.Label(text = "How many climbs are you doing for points?", fg="purple")

number = tk.IntVar()
number.set(0)
#if climb_input = "Yes"



introduction.grid(row=1, column=2, columnspan = 5)
climb_input.grid(row=3, column = 2, columnspan = 8)




root.mainloop()