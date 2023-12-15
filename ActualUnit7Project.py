# Eva D
# December 15, 2023,
# Creates a window where the user can calculate their current score in a climbing competition, based on the
# rules, structure, and scoring guidelines of the Washington Area Interscholastic Climbing League, for three different
# competition formats (bouldering, top rope, and mixed competition)

import tkinter as tk
import random

root = tk.Tk()
root.title("Climbing Comp Points Calculator")

# sets values/what type of variable for many variables used
number = tk.IntVar()
number.set(0)
selected_boulder1 = tk.StringVar()
selected_boulder2 = tk.StringVar()
selected_boulder3 = tk.StringVar()
selected_boulder4 = tk.StringVar()
selected_boulder5 = tk.StringVar()
final_score = tk.StringVar()


def determine_dropdowns():
    """
    determines which set of dropdown menus to use for the climb grades, as top rope and bouldering have different
    grading system. Gets the user input from the first dropdown asking for format, and checks input in boolean
    statements to grid the correct corresponding dropdown menus, and the correct amount of menus based on how many
    climbs each competition format requires (bouldering 3, top rope 2, mixed all five). For mixed comp, also grids
    labels to clarify which dropdown menus correspond to which climbing format.
    :return: nothing
    """
    number_of_menus = str(climb_input.get())
    menu_instructions = tk.Label(text="Select the grades of the highest-graded climbs you completed:", fg="paleturquoise")
    if number_of_menus == "Top Rope":
        menu_instructions.grid(row=6, column=2, columnspan=3)
        dropdown4.grid(row=7, column=2, columnspan=2)
        dropdown5.grid(row=7, column=3, columnspan=2)
        calculate_score_button = tk.Button(root, text="Calculate Score", command=calculate_score_ropes, fg="darkslategrey")
        calculate_score_button.grid(row=8, column=2, columnspan=3)
    elif number_of_menus == "Bouldering":
        menu_instructions.grid(row=6, column=2, columnspan=3)
        dropdown1.grid(row=7, column=2, columnspan=1)
        dropdown2.grid(row=7, column=3, columnspan=1)
        dropdown3.grid(row=7, column=4, columnspan=1)
        calculate_score_button = tk.Button(root, text="Calculate Score", command=calculate_score_boulders, fg="darkslategrey")
        calculate_score_button.grid(row=8, column=2, columnspan=3)
    elif number_of_menus == "Mixed":
        menu_instructions.grid(row=6, column=2, columnspan=5)
        climb_label_b = tk.Label(text="Boulders:", fg="white")
        climb_label_r = tk.Label(text="Ropes:", fg="white")
        climb_label_b.grid(row=7, column=2, columnspan=2)
        dropdown1.grid(row=7, column=4, columnspan=1)
        dropdown2.grid(row=7, column=5, columnspan=1)
        dropdown3.grid(row=7, column=6, columnspan=1)
        climb_label_r.grid(row=8, column=2, columnspan=2)
        dropdown4.grid(row=8, column=4, columnspan=1)
        dropdown5.grid(row=8, column=5, columnspan=1)
        calculate_score_button = tk.Button(root, text="Calculate Score", command=calculate_score_mixed, fg="darkslategrey")
        calculate_score_button.grid(row=9, column=2, columnspan=5)


def show_message():
    """
    function to generate the user a random supportive message that occurs when they click on a button asking for a
    supportive message, grids message to be at very bottom of the page
    :return: nothing
    """
    message_list = ["You can do this!", "You're doing great!", "You're awesome!", "Yippee", "You are the best climber ever!", "Yayyyyy"]
    random_number = random.randint(0, 5)
    happy_message = tk.Label(text=message_list[random_number])
    happy_message.grid(row=12, column=2, columnspan=3)


show_happy_message_button = tk.Button(root, text="Show Supportive Message", fg="darkslategrey", command=show_message)


def calculate_score_boulders():
    """
    what happens when user clicks calculate score button and had previously selected bouldering as their competition
    format. calculates the user's score by putting the selected dropdown input of what the user climbed into a list, and
    through a for loop going through every climb in that list to assign the appropriate point value based on if what is
    in the string input equals a certain string in boolean if and elif statements. the point values assigned to each
    string value are based on WAICL rules. It adds the found points to a score counter for each climb in the list, which
    is eventually output back to the user when the label in sentence format is gridded.
    :return: nothing
    """
    score = 0
    climb1 = str(selected_boulder1.get())
    climb2 = str(selected_boulder2.get())
    climb3 = str(selected_boulder3.get())
    climb_list = climb1, climb2, climb3
    for climb in climb_list:
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
    show_happy_message_button.grid(row=11, column=2, columnspan=8)


def calculate_score_ropes():
    """
    what happens when user clicks calculate score button, and they previously selected ropes format. calculates user's
    current score by putting the selected dropdown input of what the user climbed into a list, and through a
    for loop going through every climb in that list to assign the appropriate point value based on if what is in the
    string input equals a certain string in if and elif statements. the point values assigned to each string value are
    based on WAICL rules. It adds the found points to a score counter for each climb in the list, which is eventually
    gridded to output back to the user in a sentence format and gridded.
    :return: nothing
    """
    score = 0
    climb1 = str(selected_boulder3.get())
    climb2 = str(selected_boulder4.get())
    climb3 = str(selected_boulder5.get())
    climb_list = climb1, climb2, climb3
    for climb in climb_list:
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
    show_happy_message_button.grid(row=11, column=2, columnspan=8)


def calculate_score_mixed():
    """
    what happens when user clicks calculate score button, and they previously selected mixed format. calculates user's
    current score by putting the selected dropdown input of what the user climbed into a list, and through a
    for loop going through every climb in that list to assign the appropriate point value based on if what is in the
    string input equals a certain string in if and elif statements. the point values assigned to each string value are
    based on WAICL rules. It adds the found points to a score counter for each climb in the list, which is eventually
    gridded to output back to the user in a sentence format and gridded. this function has more elif statements, as some
    of the bouldering and top rope points are not a direct comparison and cannot be condensed using an "or" statement.
    :return: nothing
    """
    score = 0
    climb1 = str(selected_boulder1.get())
    climb2 = str(selected_boulder2.get())
    climb3 = str(selected_boulder3.get())
    climb4 = str(selected_boulder4.get())
    climb5 = str(selected_boulder4.get())
    climb_list = climb1, climb2, climb3, climb4, climb5
    for climb in climb_list:
        if climb == "N/A":
            points = 0
        elif climb == "V0" or climb == "5.7":
            points = 2
        elif climb == "V1" or climb == "5.8":
            points = 3
        elif climb == "V2" or climb == "5.9":
            points = 5
        elif climb == "V3" or climb == "5.10-":
            points = 7
        elif climb == "V4":
            points = 9
        elif climb == "V5" or climb == "5.11-":
            points = 11
        elif climb == "V6":
            points = 13
        elif climb == "V7" or climb == "5.12-":
            points = 15
        elif climb == "V8":
            points = 17
        elif climb == "V9":
            points = 19
        elif climb == "V10":
            points = 21
        elif climb == "5.6":
            points = 1
        elif climb == "5.10+":
            points = 10
        elif climb == "5.11+":
            points = 14
        elif climb == "5.12+":
            points = 18
        else:
            points = 0
        score = score+points
    final_score_boulders = str(score)
    score_statement = "Your current score is " + str(final_score_boulders)
    score_answer = tk.Label(text=score_statement, fg="cyan")
    score_answer.grid(row=10, column=2, columnspan=5)
    show_happy_message_button.grid(row=11, column=2, columnspan=8)


introduction = tk.Label(text="Welcome to the rock climbing competition points counter!", fg="paleturquoise")
climb_input_question = tk.Label(text="What type of competition is this?", fg="paleturquoise")
climb_input = tk.StringVar()
climb_input.set("")
# creates lists for all needed dropdown menus
dropdown0 = tk.OptionMenu(root, climb_input, "Bouldering", "Top Rope", "Mixed")
dropdown1 = tk.OptionMenu(root, selected_boulder1, "N/A", "V0", "V1", "V2", "V3", "V4", "V5", "V6", "V7", "V8", "V9", "V10")
dropdown2 = tk.OptionMenu(root, selected_boulder2, "N/A", "V0", "V1", "V2", "V3", "V4", "V5", "V6", "V7", "V8", "V9", "V10")
dropdown3 = tk.OptionMenu(root, selected_boulder3, "N/A", "V0", "V1", "V2", "V3", "V4", "V5", "V6", "V7", "V8", "V9", "V10")
dropdown4 = tk.OptionMenu(root, selected_boulder4, "N/A", "5.6", "5.7", "5.8", "5.9", "5.10-", "5.10+", "5.11-", "5.11+", "5.12-", "5.12+")
dropdown5 = tk.OptionMenu(root, selected_boulder5, "N/A", "5.6", "5.7", "5.8", "5.9", "5.10-", "5.10+", "5.11-", "5.11+", "5.12-", "5.12+")
button_for_number_of_dropdowns = tk.Button(root, text="Enter", command=determine_dropdowns, fg="darkslategrey")


introduction.grid(row=1, column=2, columnspan=5)
climb_input_question.grid(row=3, column=2, columnspan=8)
dropdown0.grid(row=4, column=2, columnspan=8)
button_for_number_of_dropdowns.grid(row=5, column=2, columnspan=8)


root.mainloop()
