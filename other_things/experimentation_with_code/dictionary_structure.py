tasks = {('Bench Press', 3, 12): {'status': 'not completed'},
('Leg Press', 4, 12): {'status': 'not completed'},
('Lateral Raises', 4, 8): {'status': 'completed'}}


# Simply collecting values
exercise_name = input("Enter the workout name: ")
sets = int(input("Enter the number of sets: "))
reps = int(input("Enter the number of reps: "))
exercise = (exercise_name, sets, reps)
tasks[exercise] = {"status": "not completed"}


exercise_name = input("Enter the workout name: ")
sets = int(input("Enter the number of sets: "))
reps = int(input("Enter the number of reps: "))
exercise = (exercise_name, sets, reps)
tasks[exercise] = {"status": "not completed"}

print(tasks)

