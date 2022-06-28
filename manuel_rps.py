from datetime import time, timedelta
import random
from random import randint
import  time
import camera_rps
from camera_rps import get_prediction

def get_computer_choice(AI_Choice = "nothing"):
    #Create a list of options and use random.choice and return the value
    AI_Options = ["Rock", "Paper", "Scissors"]
    AI_Choice = random.choice(AI_Options)
    return AI_Choice

def get_user_choice(Human_Choice = "nothing"):
    return get_prediction()
    """
    Human_Option = ["Rock","Paper","Scissors"]
    while True:
        Human_Choice = input("Enter Choice (Rock/Paper/Scissors): ")
        if Human_Choice not in Human_Option:
            print("Choice not valid.")
        else:
            return Human_Choice
            """
    pass

def get_winner(Human_Choice, AI_Choice, winner="nothing"):
    print("Human Choice: ",Human_Choice)
    print("AI Choice: ",AI_Choice)
    if Human_Choice == "Rock" and AI_Choice == "Scissors" or Human_Choice == "Paper" and AI_Choice == "Rock" or Human_Choice == "Scissors" and AI_Choice == "Paper":
        return("Human Won")
    elif AI_Choice == "Rock" and Human_Choice == "Scissors" or AI_Choice == "Paper" and Human_Choice == "Rock" or AI_Choice == "Scissors" and Human_Choice == "Paper":
        return("AI Won")
    else:
        return("Draw!")
    pass

def play():
    rounds_played = 0
    user_score = 0
    ai_score = 0
    while rounds_played < 3:
        comp_choice = get_computer_choice()
        user_choice = get_user_choice()
        winner = get_winner(user_choice, comp_choice)
        if winner != "Draw!":
            rounds_played += 1
            if winner == "Human Won":
                user_score += 1
            if winner == "AI Won":
                ai_score += 1
        if user_score == 2:
            print("You WIN!!!!")
            break
        if ai_score == 2:
            print("You LOSE!!!!")
            break
    print("User Score: ",user_score)
    print("AI Score: ", ai_score)
    pass

if __name__ == "__main__":
    play()