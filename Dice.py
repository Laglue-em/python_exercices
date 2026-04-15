import random
play = True

while play:
    roll= input ("Roll the dice ? (y/n) ").lower()

    if roll == "y":
        rolling_dice1=random.randint(1, 6)
        rolling_dice2=random.randint(1, 6)
        print (f'({rolling_dice1}/{rolling_dice2})')

    elif roll == "n":
        print("Thank you for playing !")
        break


    else:
        print("Invalid choice!")
