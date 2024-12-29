import random




while True:
    user = input("enter (y) to dice (n)to stop: ")
    if user == "y" :
        dice_one = random.randint(1, 6)
        dice_two = random.randint(1,6)
        print(f"{dice_one}, {dice_two}")
        print(dice_one+dice_two)
    elif user=="n":
        print("Thank u for playing")
        break

    else:
        print("invalid input")







