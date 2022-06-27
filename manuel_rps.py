import random
from random import randint

def get_computer_choice(AI_Choice = "nothing"):
    #Create a list of options and use random.choice and return the value
    AI_Options = ["Rock", "Paper", "Scissors"]
    AI_Choice = random.choice(AI_Options)
    return AI_Choice

def get_user_choice(Human_Choice = "nothing"):
    Human_Option = ["Rock","Paper","Scissors"]
    while True:
        Human_Choice = input("Enter Choice (Rock/Paper/Scissors): ")
        if Human_Choice not in Human_Option:
            print("Choice not valid.")
        else:
            return Human_Choice
    pass

def get_winner(Human_Choice, AI_Choice):
    print("Human Choice: ",Human_Choice)
    print("AI Choice: ",AI_Choice)
    if Human_Choice == "Rock" and AI_Choice == "Scissors" or Human_Choice == "Paper" and AI_Choice == "Rock" or Human_Choice == "Scissors" and AI_Choice == "Paper":
        print("Human Won")
    elif AI_Choice == "Rock" and Human_Choice == "Scissors" or AI_Choice == "Paper" and Human_Choice == "Rock" or AI_Choice == "Scissors" and Human_Choice == "Paper":
        print("AI Won")
    else:
        print("Draw!")
    pass

def play():
    get_winner(get_user_choice(), get_computer_choice())
    pass
if __name__ == "__main__":
    play()
    pass