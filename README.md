# Computer-Vision-Rock-Paper-Scissors

>Creating a Rock, Paper and Scissors game using Computer Vision.

# Controls

>Press a to start the game.
>Use the camera to determine your input.
>For each round you play, press n to go to the next round.

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

>Make sure camera is not in use before running the code else it cannot detect if a camera exists. And make sure you have a camera


Created a manual rock paper scissors game in python with 3 functions: get_computer_choice, get_user_choice and get_winner.
get_computer_choice is a function which returns either Rock, Paper or Scissors using the random method.


get_user_choice is a function where it asks the user to input a choice and returns the choice. It loops around until the user have inputed a valid choice.

get_winner is a function which requires 2 str arguments (A human choice and a computer choice) and prints out the winner.

The human choice function is then replaced with a get_prediction function which compares the proablility of each class in the model. The highest probability will be used as the human input.

The game is replayable when reaching the end of the game.

