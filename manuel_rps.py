import random
from random import randint

def get_prediction(prediction):
    if prediction[0][0] > 0.5:
        return('Rock')
    elif prediction[0][1] > 0.5:
        return('Paper')
    elif prediction[0][2] > 0.5:
        return('Scissors')
    else:
        return('Nothing')
    
def get_computer_choice(AI_Choice = "nothing"):
    #Create a list of options and use random.choice and return the value
    AI_Options = ["Rock", "Paper", "Scissors"]
    AI_Choice = random.choice(AI_Options)
    return AI_Choice

def get_user_choice(predict):
    return get_prediction(predict)

def get_winner(Human_Choice, AI_Choice):
    print("Human Choice: ",Human_Choice)
    print("AI Choice: ",AI_Choice)
    if Human_Choice == "Rock" and AI_Choice == "Scissors" or Human_Choice == "Paper" and AI_Choice == "Rock" or Human_Choice == "Scissors" and AI_Choice == "Paper":
        return("Human Won")
    elif AI_Choice == "Rock" and Human_Choice == "Scissors" or AI_Choice == "Paper" and Human_Choice == "Rock" or AI_Choice == "Scissors" and Human_Choice == "Paper":
        return("AI Won")
    else:
        return("Draw!")

def play(prediction, winner=""):
    comp_choice = get_computer_choice()
    user_choice = get_user_choice(prediction)
    winner = get_winner(user_choice, comp_choice)
    return winner