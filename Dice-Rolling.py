import random

while True:
    choice = input("Do you want to roll the dice? y/n: ")
    if choice == "y":
        dice1 = random.randint(1,6)
        dice2 = random.randint(1,6)
        print(f"You rolled {dice1} and {dice2}.")
    elif choice == "n":
        print("You stopped playing.")
        break
    else:
        print("Invalid choice.")