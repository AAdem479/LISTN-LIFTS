# homepage_func.py
def homepage():
    print("You are now using AA-Fitness!",
          "\nA. to add an exercise",
          "\nB. to remove a planned exercise",
          "\nC. to checkmark exercise as complete",
          "\nD. to update exercise as incomplete",
          "\nE. to see your entire workout",
          "\nF. to see your planned exercise(s)",
          "\nG. to see your completed exercise(s)",
          "\nH. to edit an exercise's name",
          "\nI. to edit the amount of sets of an exercise",
          "\nJ. to edit the amount of reps of an exercise",
          "\nK. to exit the app")

    choice = input("Please select a (A/B/C/D/E/F/G/H)!: ")
    return choice
