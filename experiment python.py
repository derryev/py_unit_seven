

import tkinter as tk

root = tk.Tk()
root.title("Climbing Score Calculator")

boulders_list = ["Vintro", "V0", "V1", "V2", "V3", "V4", "V5", "V6", "V7", "V8", "V9", "V10"]
selected_boulder1 = tk.StringVar()
selected_boulder2 = tk.StringVar()
selected_boulder3 = tk.StringVar()

introduction = tk.Label(text = "Welcome to the bouldering competition points counter!", fg="magenta")

def determine_dropdowns():
    hello = 10
    number_of_menus = int(climb_input.get())
    menu_instructions = tk.Label(text="Select the grades of the highest-graded climbs you completed:",fg="magenta")
    menu_instructions.grid(row=6,column=2,columnspan=3)
    if number_of_menus == 2:
        ## I learned how to make a dropdown menu from https://www.tutorialsfreak.com/python-tutorial/drop-down-menus-in-python-tkinter, but I did the grid myself.
        dropdown1 = tk.OptionMenu(root, selected_boulder1, "Vintro", "V0", "V1", "V2", "V3", "V4", "V5",
                                  "V6","V7", "V8", "V9", "V10")
        dropdown2 = tk.OptionMenu(root, selected_boulder2, "Vintro", "V0", "V1", "V2", "V3", "V4", "V5",
                                  "V6", "V7", "V8", "V9", "V10")
        dropdown1.grid(row=7, column=2, columnspan=2)
        dropdown2.grid(row=7, column=3, columnspan=2)
    elif number_of_menus == 3:
        dropdown1 = tk.OptionMenu(root, selected_boulder1, "Vintro", "V0", "V1", "V2", "V3", "V4", "V5",
                                  "V6", "V7", "V8", "V9", "V10")
        dropdown2 = tk.OptionMenu(root, selected_boulder2, "Vintro", "V0", "V1", "V2", "V3", "V4", "V5",
                                  "V6", "V7", "V8", "V9", "V10")
        dropdown3 = tk.OptionMenu(root, selected_boulder3, "Vintro", "V0", "V1", "V2", "V3", "V4", "V5",
                                  "V6", "V7", "V8", "V9", "V10")
        dropdown1.grid(row=7, column=2, columnspan=3)
        dropdown2.grid(row=7, column=3, columnspan=3)
        dropdown3.grid(row=7, column=4, columnspan=3)


def calculate_score():
    climb1 = str(selected_boulder1.get)
    climb2 = selected_boulder2
    climb3 = selected_boulder3
    print(climb1)
    print(climb2)



climb_input_question = tk.Label(text = "Are you entering 2 or 3 climbs?", fg="magenta")
climb_input = tk.StringVar()
climb_input.set("2")
climb_input_entry = tk.Entry(root, textvariable=climb_input, fg = "cyan")
button_for_number_of_dropdowns = tk.Button(root, text="Enter", command=determine_dropdowns,fg="magenta")

number = tk.IntVar()
number.set(0)

calculate_score_button = tk.Button(root, text="Calculate Total Score", command=calculate_score, fg="magenta")


introduction.grid(row=1, column=2, columnspan = 5)
climb_input_question.grid(row=3, column = 2, columnspan = 8)
climb_input_entry.grid(row=4, column = 2, columnspan=8)
button_for_number_of_dropdowns.grid(row=5,column=2,columnspan=8)
calculate_score_button.grid(row=8,column=2,columnspan=3)
# dropdown.grid(row=7, column=2,columnspan=8)




root.mainloop()