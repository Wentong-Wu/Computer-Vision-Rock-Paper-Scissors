from asyncio.windows_events import NULL
from statistics import mode
import cv2
from keras.models import load_model
import numpy as np
import time
from manuel_rps import play

model = load_model('keras_model.h5')
cap = cv2.VideoCapture(0)
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
cdTime = float(5.0)
startGame = False
stopGame = False
gameRound = 0
human_score = 0
ai_score = 0
while True:
    #Display the camera
    ret, frame = cap.read()
    resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
    image_np = np.array(resized_frame)
    normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
    data[0] = normalized_image
    prediction = model.predict(data)
    
    #Play the game
    if startGame == False:
        print("Press 'a' to start game")
    if cv2.waitKey(33) == ord('a') and startGame == False:
        startTime = time.time()
        startGame = True
    if startGame == True:
        currentTime = time.time() - startTime
        print(currentTime)
        if (currentTime > cdTime) and stopGame == False:
            winner = play(prediction)
            if winner == "Human Won":
                human_score += 1
                gameRound += 1
            elif winner == "AI Won":
                ai_score += 1
                gameRound += 1
            stopGame = True
        if stopGame == True:
            if human_score == 3:
                print("You Win!")
                stopGame = False
                startGame = False
            elif ai_score == 3:
                print("You Lose!")
                stopGame = False
                startGame = False
            print("Press 'n' for next match")
            if cv2.waitKey(33) == ord('n'):
                startTime = time.time()
                stopGame = False
    #End of the game
    cv2.imshow('frame', frame)
    # Press q to close the window
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
            
# After the loop release the cap object
cap.release()
# Destroy all the windows
cv2.destroyAllWindows()