import random
number_to_guess=random.randint(1, 100)

while True:
    try:
        guessing =int(input ("Guess the number between 1 and 100 : "))

        if guessing < number_to_guess:
            print ("Too low")

        elif guessing > number_to_guess:
            print ("Too high")

        else:
            print("Congratulation ! You guess the number !")
            break
    except ValueError:
        print("Please enter a valid number !")
        
