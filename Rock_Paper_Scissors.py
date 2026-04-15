import random

emoji={"r": "🪨", "p":"📄", "s":"✂️"}
choices=("r","s","p")

while True:
    my_choice= input ("Rock Paper or Scissors ? (r/s/p): ").lower()

    if my_choice not in choices:
        print ("Invalid choice")
        continue

    computer_choice=random.choice(choices)

    print (f"You chose {emoji[my_choice]}")
    print (f"Computer chose {emoji[computer_choice]}")

    if my_choice == computer_choice:
        print ("Ex æquo")
    elif my_choice == "r" and computer_choice == "s":
        print("You win !")
    elif my_choice == "s" and computer_choice == "r":
        print("Computer win!")
    elif my_choice == "p" and computer_choice == "r":
        print("You win")
    elif my_choice == "r" and computer_choice == "p":
        print("Computer win!")
    elif my_choice == "p" and computer_choice == "s":
        print("Computer win!")
    elif my_choice == "s" and computer_choice =="p":
        print("You win!")
    else:
        print("You lose")

    end_game=input("You want to continue ?(y/n): ").lower()
    if end_game == "n":
        print ("Bye bye ! See you soon !")
        break
