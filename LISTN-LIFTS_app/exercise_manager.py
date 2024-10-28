from data import exercises
from exercise_displays import display_exercises


# anti-duplication functions


def show_exercises():
    if len(exercises) == 0:
        print("You currently have no planned exercises.")
        return False
    else:
        print("Your exercises are:")
        for i, (workout, status) in enumerate(exercises.items(), 1):
            print(f"{i}: Workout: {workout[0]}, Sets: {workout[1]}, Reps: {workout[2]}, Status: {status['status']}")
        return True


def return_choice():
    while True:
        choice = input("Please enter the number of the exercise you'd like to modify: ").strip()
        if choice.isdigit() and 1 <= int(choice) <= len(exercises):
            return int(choice) - 1
        else:
            print("Please input a valid exercise number.")


# whole exercise manipulation


def add_exercise():
    exercise_name = input("Enter the workout name: ")
    sets = int(input("Enter the number of sets: "))
    reps = int(input("Enter the number of reps: "))

    exercise = (exercise_name, sets, reps)

    exercises[exercise] = {"status": "not completed"}

    print("Task added successfully!")
    display_exercises(status=None)


def remove_exercise():
    if show_exercises():
        choice = return_choice()
        exercise_to_remove = list(exercises.keys())[choice]
        exercises.pop(exercise_to_remove)
        print(f"Task '{exercise_to_remove}' removed successfully!")
    else:
        print("Invalid task number.")


def update_exercise_complete():
    if show_exercises():
        choice = return_choice()
        exercise_to_complete = list(exercises.keys())[choice]
        exercises[exercise_to_complete]["status"] = "completed"
        print(f"Task '{exercise_to_complete}' marked as complete successfully!")
    else:
        print("Invalid task number.")


def update_exercise_incomplete():
    if show_exercises():
        choice = return_choice()
        exercise_to_incomplete = list(exercises.keys())[choice]
        exercises[exercise_to_incomplete]["status"] = "not completed"
        print(f"Exercise '{exercise_to_incomplete}' marked as incomplete successfully!")
    else:
        print("Invalid task number.")


# inner exercise manipulation


def general_exercise_editing(item):
    if not show_exercises():
        return
    choice = return_choice()
    chosen_exercise = list(exercises.keys())[choice]
    key_position = exercises.pop(chosen_exercise)
    match item:
        case "exercise_name":
            name_to_edit = list(chosen_exercise)
            name_to_edit[0] = input(str("What would you like to rename this exercise to?: "))
            new_name = tuple(name_to_edit)

            exercises[new_name] = key_position
            print(f"Exercise '{chosen_exercise[0]}' renamed successfully to {new_name[0]}!")

        case "exercise_sets":
            sets_to_edit = list(chosen_exercise)
            sets_to_edit[1] = int(input(f"What would you like to change your sets amount to?: "))
            new_sets_amount = tuple(sets_to_edit)

            exercises[new_sets_amount] = key_position

            print(f"Sets updated from '{chosen_exercise[1]}' to {new_sets_amount[1]} for {chosen_exercise[0]}!")

        case "exercise_reps":
            reps_to_edit = list(chosen_exercise)
            reps_to_edit[2] = int(input("What would you like to change your reps amount to?: "))
            new_reps_amount = tuple(reps_to_edit)

            exercises[new_reps_amount] = key_position
            print(f"Reps updated from '{chosen_exercise[2]}' to {new_reps_amount[2]} for {chosen_exercise[0]}!")
