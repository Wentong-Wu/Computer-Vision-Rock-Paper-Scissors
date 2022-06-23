# Computer-Vision-Rock-Paper-Scissors

>Creating a Rock, Paper and Scissors game using Computer Vision.

## Setting Up The Project

Software Used:

-Visual Studio Code

-Ubuntu

-Python

-Tensorflow

-Download Keras Model and Add Labels for Rock, Paper, Scissors and nothing

Virtual environment is a version control system which seperates from each environment

## Setting Up Virtual Environment

Created the Virtual Environment in Visual Studio Code using the terminal with the following command line:Python3 -m venv {EnvironmentName}.

Activate the environment using the following command: {EnvironmentName}/Scripts/activate. This activates the environment which means that you are currently using the version of the environment you just activated.

Then make sure to have the following librarys: 

  -pip install opencv-python
  
  -pip install tensorflow
  
  -pip install ipykernel
  
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
