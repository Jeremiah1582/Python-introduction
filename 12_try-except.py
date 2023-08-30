# in this script we will learn how to use a Try Catch Block



input_is_valid = False

while (not input_is_valid):
    try:
        userInput = int(input("What's your age?: "))
        if userInput < 13:
            print("You are too young, please wait couple of years")
        elif userInput > 13 and userInput < 30:
            print("Welcome to the fitness studio!!")
        else:
            print("You have to go to a special fitness studio")

    except ValueError:
        print("Invalid input")
        continue
    input_is_valid = True