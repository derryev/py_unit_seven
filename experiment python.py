

import tkinter as tk

root = tk.Tk()
root.title("Climbing Score Calculator")

number = tk.IntVar()
number.set(0)

boulders_list = ["Vintro", "V0", "V1", "V2", "V3", "V4", "V5", "V6", "V7", "V8", "V9", "V10"]
selected_boulder1 = tk.StringVar()
selected_boulder2 = tk.StringVar()
selected_boulder3 = tk.StringVar()
final_score = tk.StringVar()



def determine_dropdowns():
    number_of_menus = int(climb_input.get())
    menu_instructions = tk.Label(text="Select the grades of the highest-graded climbs you completed:", fg="magenta")
    menu_instructions.grid(row=6, column=2, columnspan=3)
    if number_of_menus == 2:
        dropdown1.grid(row=7, column=2, columnspan=2)
        dropdown2.grid(row=7, column=3, columnspan=2)
    elif number_of_menus == 3:
        dropdown1.grid(row=7, column=2, columnspan=3)
        dropdown2.grid(row=7, column=3, columnspan=3)
        dropdown3.grid(row=7, column=4, columnspan=3)


def calculate_score():
    score = 0
    climb1 = str(selected_boulder1.get())
    climb2 = str(selected_boulder2.get())
    climb3 = str(selected_boulder3.get())
    climb_list = climb1, climb2, climb3
    # print(climb_list)
    for climb in climb_list:
        # print(climb)
        if climb == "Vintro":
            points = 0
        elif climb == "V0":
            points = 2
        elif climb == "V1":
            points = 3
        elif climb == "V2":
            points = 5
        elif climb == "V3":
            points = 7
        elif climb == "V4":
            points = 9
        elif climb == "V5":
            points = 11
        elif climb == "V6":
            points = 13
        elif climb == "V7":
            points = 15
        elif climb == "V8":
            points = 17
        elif climb == "V9":
            points = 19
        elif climb == "V10":
            points = 21
        else:
            points = 0
        score = score+points
    final_score = str(score)
    return final_score


introduction = tk.Label(text="Welcome to the bouldering competition points counter!", fg="magenta")
climb_input_question = tk.Label(text="Are you entering 2 or 3 climbs?", fg="magenta")
climb_input = tk.StringVar()
climb_input.set("2")
climb_input_entry = tk.Entry(root, textvariable=climb_input, fg = "cyan")
number_of_menus = int(climb_input.get())
dropdown1 = tk.OptionMenu(root, selected_boulder1, "Vintro", "V0", "V1", "V2", "V3", "V4", "V5", "V6", "V7", "V8", "V9", "V10")
dropdown2 = tk.OptionMenu(root, selected_boulder2, "Vintro", "V0", "V1", "V2", "V3", "V4", "V5", "V6", "V7", "V8", "V9", "V10")
dropdown3 = tk.OptionMenu(root, selected_boulder3, "Vintro", "V0", "V1", "V2", "V3", "V4", "V5", "V6", "V7", "V8", "V9", "V10")
button_for_number_of_dropdowns = tk.Button(root, text="Enter", command=determine_dropdowns,fg="magenta")
calculate_score_button = tk.Button(root, text="Calculate Total Score", command=calculate_score, fg="magenta")
score_statement = "Your current score is "+str(final_score.get())
score_answer = tk.Label(text=score_statement,fg="magenta")


introduction.grid(row=1, column=2, columnspan = 5)
climb_input_question.grid(row=3, column = 2, columnspan = 8)
climb_input_entry.grid(row=4, column = 2, columnspan=8)
button_for_number_of_dropdowns.grid(row=5,column=2,columnspan=8)
calculate_score_button.grid(row=8,column=2,columnspan=3)
score_answer.grid(row=10,column=2,columnspan=3)
# dropdown.grid(row=7, column=2,columnspan=8)




root.mainloop()