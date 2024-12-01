from data import exercises
from exercise_displays import display_exercises
from datetime import date


# anti-duplication functions


def show_exercises():
    if len(exercises) == 0:    # needing to make sure there are exercises
        print("You currently have no planned exercises.")
        return False # false if dictionary is empty
    else:
        print("Your exercises are: ")
        for i, (workout, status) in enumerate(exercises.items(), 1):  # display with enumeration
            print(f"{i}: Workout: {workout[0]}, Sets: {workout[1]}, Reps: {workout[2]}, Status: {status['status']}")
        return True


def return_choice():
    while True:
        choice = input("Please enter the number of the exercise you'd like to modify: ").strip() # taking user's digit input
        if choice.isdigit() and 1 <= int(choice) <= len(exercises): # validating it, needs to meet the set condition
            return int(choice) - 1 # account for indexing
        else:
            print("Please input a valid exercise number.")


# whole exercise manipulation


def add_exercise():
    exercise_name = input("Enter the workout name: ")
    sets = int(input("Enter the number of sets: "))
    reps = int(input("Enter the number of reps: "))
    today = date.today()
    formatted_today = today.strftime('%b-%d-%Y')

    exercise = (exercise_name, sets, reps, formatted_today) # adds item to exercise dictionary based on previous inputs 

    exercises[exercise] = {"status": "not completed"} # if exercise was just added, of course it's incomplete

    print("Exercise added successfully!")
    display_exercises(status=None) # display all exercises without a status, so all


def remove_exercise():
    if show_exercises(): # see show_exercises() above, we call it here. if it returns false (no exercises) it stops
        choice = return_choice() # see return_choice() above, getting user choice
        exercise_to_remove = list(exercises.keys())[choice] # list the keys in the dictionary, and index
        exercises.pop(exercise_to_remove) # popped
        print(f"Exercise '{exercise_to_remove}' removed successfully!")
    else:
        print("Invalid exercise number.")


def update_exercise_complete():
    if show_exercises():
        choice = return_choice()
        exercise_to_complete = list(exercises.keys())[choice]
        exercises[exercise_to_complete]["status"] = "completed" # same process as above but the change is the status
        print(f"Exercise '{exercise_to_complete}' marked as complete successfully!")
    else:
        print("Invalid exercise number.")


def update_exercise_incomplete():
    if show_exercises():
        choice = return_choice()
        exercise_to_incomplete = list(exercises.keys())[choice]
        exercises[exercise_to_incomplete]["status"] = "not completed" # still changing the exercise status but to incomplete
        print(f"Exercise '{exercise_to_incomplete}' marked as incomplete successfully!")
    else:
        print("Invalid exercise number.")


# inner exercise manipulation


def general_exercise_editing(item):
    if not show_exercises():
        return
    choice = return_choice()
    chosen_exercise = list(exercises.keys())[choice]
    key_position = exercises.pop(chosen_exercise) # popping the exercise but keeping key position
    match item: # used case matching instead of if else for optimization purposes
        case "exercise_name":
            name_to_edit = list(chosen_exercise)
            name_to_edit[0] = input(str("What would you like to rename this exercise to?: ")) # [0] in the dictionary's structure is the exercise_name
            new_name = tuple(name_to_edit)

            exercises[new_name] = key_position
            print(f"Exercise '{chosen_exercise[0]}' renamed successfully to {new_name[0]}!") # informing user the task is complete, while mentioning old name

        case "exercise_sets":
            sets_to_edit = list(chosen_exercise)
            sets_to_edit[1] = int(input(f"What would you like to change your sets amount to?: ")) # [1] exercise_sets
            new_sets_amount = tuple(sets_to_edit)

            exercises[new_sets_amount] = key_position

            print(f"Sets updated from '{chosen_exercise[1]}' to {new_sets_amount[1]} for {chosen_exercise[0]}!") # old amount to new amount, could be the same

        case "exercise_reps":
            reps_to_edit = list(chosen_exercise)
            reps_to_edit[2] = int(input("What would you like to change your reps amount to?: ")) # [2] exercise_reps 
            new_reps_amount = tuple(reps_to_edit)

            exercises[new_reps_amount] = key_position
            print(f"Reps updated from '{chosen_exercise[2]}' to {new_reps_amount[2]} for {chosen_exercise[0]}!")
