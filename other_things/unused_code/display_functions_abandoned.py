'''def display_all_exercises():
    if len(exercises) == 0:
        print("No exercises found.")
    else:
        print("Your tasks are:")
        for i, (workout, status) in enumerate(exercises.items(), 1):
            print(f"{i}: Workout: {workout[0]}, Sets: {workout[1]}, Reps: {workout[2]}, Status: {status['status']}")


def display_completed_exercises():
    if len(exercises) == 0:
        print("No exercises found.")
    else:
        print("Your finished tasks are:")
        for i, (exercise_details, current_status) in enumerate(exercises.items(), 1):
            exercise_name, sets, reps = exercise_details
            if current_status['status'] == "completed":
                print(f"{i}: Workout: {exercise_name}, Sets: {sets}, Reps: {reps}, Status: {current_status['status']}")


def display_incomplete_exercises():
    if len(exercises) == 0:
        print("No exercises found.")
    else:
        print("Your finished tasks are:")

        for i, (exercise_details, current_status) in enumerate(exercises.items(), 1):
            exercise_name, sets, reps = exercise_details
            if current_status['status'] == "not completed":
                print(f"{i}: Workout: {exercise_name}, Sets: {sets}, Reps: {reps}, Status: {current_status['status']}")'''