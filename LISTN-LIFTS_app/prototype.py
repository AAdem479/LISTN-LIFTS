# main.py
from homepage_func import homepage
from exercise_manager import add_exercise, remove_exercise, update_exercise_complete, update_exercise_incomplete
from exercise_manager import general_exercise_editing
from exercise_displays import display_exercises


def prototype():
    while True:
        choice = homepage()
        match choice.casefold():
            case "a":
                add_exercise()
            case "b":
                remove_exercise()
            case "c":
                update_exercise_complete()
            case "d":
                update_exercise_incomplete()
            case "e":
                display_exercises(status=None)
            case "f":
                display_exercises(status="not completed")
            case "g":
                display_exercises(status="completed")
            case "h":
                general_exercise_editing(item="exercise_name")
            case "i":
                general_exercise_editing(item="exercise_sets")
            case "j":
                general_exercise_editing(item="exercise_reps")
            case "k":
                print("Thank you for using LISTN'LIFTS! Goodbye.")
                break
            case _:
                print("Please input a valid option.")


if __name__ == "__main__":
    prototype()
