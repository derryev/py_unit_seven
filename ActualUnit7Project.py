

# hello what

import tkinter as tk

root = tk.Tk()
root.title("Climbing Comp Points Calculator")

number = tk.IntVar()
number.set(0)
selected_boulder1 = tk.StringVar()
selected_boulder2 = tk.StringVar()
selected_boulder3 = tk.StringVar()
selected_boulder4 = tk.StringVar()
selected_boulder5 = tk.StringVar()
final_score = tk.StringVar()


def determine_dropdowns():
    number_of_menus = str(climb_input.get())
    menu_instructions = tk.Label(text="Select the grades of the highest-graded climbs you completed:", fg="magenta")
    menu_instructions.grid(row=6, column=2, columnspan=3)
    if number_of_menus == "Top Rope":
        dropdown4.grid(row=7, column=1, columnspan=3)
        dropdown5.grid(row=7, column=3, columnspan=3)
        calculate_score_button = tk.Button(root, text="Calculate Score", command=calculate_score_ropes, fg="magenta")
        calculate_score_button.grid(row=8, column=2, columnspan=3)
    elif number_of_menus == "Bouldering":
        dropdown1.grid(row=7, column=1, columnspan=3)
        dropdown2.grid(row=7, column=2, columnspan=3)
        dropdown3.grid(row=7, column=3, columnspan=3)
        calculate_score_button = tk.Button(root, text="Calculate Score", command=calculate_score_boulders, fg="magenta")
        calculate_score_button.grid(row=8, column=2, columnspan=3)


def calculate_score_boulders():
    score = 0
    climb1 = str(selected_boulder1.get())
    climb2 = str(selected_boulder2.get())
    climb3 = str(selected_boulder3.get())
    climb_list = climb1, climb2, climb3
    # print(climb_list)
    for climb in climb_list:
        # print(climb)
        if climb == "N/A":
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
    final_score_boulders = str(score)
    score_statement = "Your current score is " + str(final_score_boulders)
    score_answer = tk.Label(text=score_statement, fg="cyan")
    score_answer.grid(row=10, column=2, columnspan=3)


def calculate_score_ropes():
    score = 0
    climb1 = str(selected_boulder3.get())
    climb2 = str(selected_boulder4.get())
    climb3 = str(selected_boulder5.get())
    climb_list = climb1, climb2, climb3
    # print(climb_list)
    for climb in climb_list:
        # print(climb)
        if climb == "N/A":
            points = 0
        elif climb == "5.6":
            points = 1
        elif climb == "5.7":
            points = 2
        elif climb == "5.8":
            points = 3
        elif climb == "5.9":
            points = 5
        elif climb == "5.10-":
            points = 7
        elif climb == "5.10+":
            points = 10
        elif climb == "5.11-":
            points = 11
        elif climb == "5.11+":
            points = 14
        elif climb == "5.12-":
            points = 15
        elif climb == "5.12+":
            points = 18
        else:
            points = 0
        score = score+points
    final_score_ropes = str(score)
    score_statement = "Your current score is " + str(final_score_ropes)
    score_answer = tk.Label(text=score_statement, fg="cyan")
    score_answer.grid(row=10, column=2, columnspan=3)


introduction = tk.Label(text="Welcome to the rock climbing competition points counter!", fg="magenta")
climb_input_question = tk.Label(text="Is this a bouldering or top rope competition?", fg="magenta")
climb_input = tk.StringVar()
climb_input.set("")
dropdown0 = tk.OptionMenu(root, climb_input, "Bouldering", "Top Rope")
# number_of_menus = str(climb_input.get())
dropdown1 = tk.OptionMenu(root, selected_boulder1, "N/A", "V0", "V1", "V2", "V3", "V4", "V5", "V6", "V7", "V8", "V9", "V10")
dropdown2 = tk.OptionMenu(root, selected_boulder2, "N/A", "V0", "V1", "V2", "V3", "V4", "V5", "V6", "V7", "V8", "V9", "V10")
dropdown3 = tk.OptionMenu(root, selected_boulder3, "N/A", "V0", "V1", "V2", "V3", "V4", "V5", "V6", "V7", "V8", "V9", "V10")
dropdown4 = tk.OptionMenu(root, selected_boulder4, "N/A", "5.6", "5.7", "5.8", "5.9", "5.10-", "5.10+", "5.11-", "5.11+", "5.12-", "5.12+")
dropdown5 = tk.OptionMenu(root, selected_boulder5, "N/A", "5.6", "5.7", "5.8", "5.9", "5.10-", "5.10+", "5.11-", "5.11+", "5.12-", "5.12+")
button_for_number_of_dropdowns = tk.Button(root, text="Enter", command=determine_dropdowns, fg="magenta")


introduction.grid(row=1, column=2, columnspan=5)
climb_input_question.grid(row=3, column=2, columnspan=8)
dropdown0.grid(row=4, column=2, columnspan=8)
button_for_number_of_dropdowns.grid(row=5, column=2, columnspan=8)


root.mainloop()
