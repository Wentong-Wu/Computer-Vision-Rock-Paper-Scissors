# Computer-Vision-Rock-Paper-Scissors

>Creating a Rock, Paper and Scissors game using Computer Vision.

## Setting Up The Project

Software Used:

>Virtual environment is a version control system which seperates from each environment

-Visual Studio Code

-Python

-Tensorflow

-Download Keras Model and Add Labels for Rock, Paper, Scissors and nothing

## Setting Up Virtual Environment

Created the Virtual Environment in Visual Studio Code using the terminal with the following command line:
>Python3 -m venv {EnvironmentName}.

Activate the environment using the following command: {EnvironmentName}/Scripts/activate. This activates the environment which means that you are currently using the version of the environment you just activated.

Then make sure to have the following librarys: 

>pip install opencv-python
  
>pip install tensorflow
  
>pip install ipykernel
  
Environment is now set up! It is ready to be used.

Firstly, I created a new python file named it 'Test.py' this file is used to test to see if the keras model has set up correctly and working using the Keras Model.
```python
import cv2
from keras.models import load_model
import numpy as np
model = load_model('keras_model.h5')
cap = cv2.VideoCapture(0)
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

while True: 
    ret, frame = cap.read()
    resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
    image_np = np.array(resized_frame)
    normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
    data[0] = normalized_image
    prediction = model.predict(data)
    cv2.imshow('frame', frame)
    # Press q to close the window
    print(prediction)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
            
# After the loop release the cap object
cap.release()
# Destroy all the windows
cv2.destroyAllWindows()
```

Created a manual rock paper scissors game in python with 3 functions: get_computer_choice, get_user_choice and get_winner.
get_computer_choice is a function which returns either Rock, Paper or Scissors using the random method.
```python
import random
from random import randint

def get_computer_choice(AI_Choice = "nothing"):
    #Create a list of options and use random.choice and return the value
    AI_Options = ["Rock", "Paper", "Scissors"]
    AI_Choice = random.choice(AI_Options)
    return AI_Choice
```

get_user_choice is a function where it asks the user to input a choice and returns the choice. It loops around until the user have inputed a valid choice.
```python
def get_user_choice(Human_Choice = "nothing"):
    Human_Option = ["Rock","Paper","Scissors"]
    while True:
        Human_Choice = input("Enter Choice (Rock/Paper/Scissors): ")
        if Human_Choice not in Human_Option:
            print("Choice not valid.")
        else:
            return Human_Choice
    pass
```

get_winner is a function which requires 2 str arguments (A human choice and a computer choice) and prints out the winner.
```python
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
```
