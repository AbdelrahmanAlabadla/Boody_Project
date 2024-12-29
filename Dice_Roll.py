import random  # Import the random module
# Start a loop to roll the dice
while True:
    # Ask the user for input
    user = input("Enter (y) to roll the dice, (n) to stop: ")

    # If the user inputs 'y', roll the dice
    if user == "y":
        # Use randint() to choose a random number between 1 and 6 for each die
        dice_one = random.randint(1, 6)
        dice_two = random.randint(1, 6)

        # Print the result of the roll
        print(f"{dice_one}, {dice_two}")

        # Print the sum of the two dice
        print("Total:",dice_one + dice_two)
       

    # If the user inputs 'n', stop the game
    elif user == "n":
        # Print a thank you message to the user
        print("Thank you for playing!")

        # Break the loop to end the game
        break

    # If the user enters an invalid input
    else:
        print("Invalid input")
