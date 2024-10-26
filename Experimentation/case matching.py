# main.py
from homepage_func import homepage
from exercise_manager import add_exercise, remove_exercise, update_exercise_complete, update_exercise_incomplete
from exercise_displays import display_all_exercises, display_completed_exercises, display_incomplete_exercises


def prototype():
    while True:
        choice = homepage()
        match choice:
            case "a":
                add_exercise()
            case "b":
                remove_exercise()
            case "d":
                update_exercise_complete()
            case "d":
                update_exercise_incomplete()
            case "e":
                display_all_exercises()
            case "f":
                display_incomplete_exercises()
            case "g":
                display_completed_exercises()
            case "H":
                print("Thank you for using AA-Fitness! Goodbye.")
                break
            case _:
                print("Please input a valid option.")


if __name__ == "__main__":
    prototype()
