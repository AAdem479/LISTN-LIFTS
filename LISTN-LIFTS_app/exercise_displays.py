# exercise_displays.py
from data import exercises


def display_exercises(status):
    if len(exercises) == 0: # checking if dictionary has keys
        print("No exercises found.")
    match status: # match casing instead of if else statements
        case "completed": 
            print("Your finished exercises are: ")
        case "not completed":
            print("You still have to do: ")
        case None:
            print("Your exercises for the day are: ")
    for i, (exercise_details, current_status) in enumerate(exercises.items(), 1):
        exercise_name, sets, reps = exercise_details
        if status is None: # outputs ALL exercises regardless of status
            print(f"{i}: Workout: {exercise_name}, Sets: {sets}, Reps: {reps}, Status: {current_status['status']}")
        elif current_status['status'] == status: # outputs exercises based on status = ("completed" or "not completed")
            print(f"{i}: Workout: {exercise_name}, Sets: {sets}, Reps: {reps}, Status: {current_status['status']}")
