# Abandoned

tasks = {}

def add_workout():
    task_to_add = input("What task would you like to add?: ")
    sets = input("For how many sets?: ")
    reps = input("How many reps would you like to assign to this task?: ")

    try:
        reps = int(reps)
        sets = int(sets)
    except ValueError:
        print("Please enter a valid number for reps.")
        return

    tasks[task_to_add] = {'sets': sets, 'reps': reps}
    print("Task added successfully!")

    display_task()

def display_task():
    if len(tasks) == 0:
        print("You have no tasks yet.")
    else:
        print("Your tasks are:")
        for task, details in tasks.items():
            print(f"{task}: {details['sets']} sets, for {details['reps']} reps")


add_workout()