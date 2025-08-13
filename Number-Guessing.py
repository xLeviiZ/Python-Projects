import random

number = random.randint(1,10)

while True:
    guess = int(input("Guess the number from 1 to 100: "))
    if guess == number:
        while True:
            again = input("You guessed it! Wanna go again? y/n: ")
            if again == "y":
                number = random.randint(1,100)
                continue
            elif again == "n":
                print("You stopped the game.")
                exit()
            else:
                print("Invalid choice.")
    elif guess != number:
        print("Wrong guess, try again.")
    else:
        print("Invalid guess.")