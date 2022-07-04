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
org = (50,50)
font = cv2.FONT_HERSHEY_SIMPLEX
colour = (255,0,0)
winner = ''
gamewinner = ''
while True:
    #Display the camera
    ret, frame = cap.read()
    resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
    image_np = np.array(resized_frame)
    normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
    data[0] = normalized_image
    prediction = model.predict(data)
    cv2.putText(frame,f'Round: {gameRound}',(50,100),font,1,colour,2,cv2.LINE_AA)
    cv2.putText(frame,f'Human won: {human_score}',(50,150),font,1,colour,2,cv2.LINE_AA)
    cv2.putText(frame,f'Computer won: {ai_score}',(50,200),font,1,colour,2,cv2.LINE_AA)
    cv2.putText(frame,f'{gamewinner}',(50,250),font,1,colour,2,cv2.LINE_AA)
    cv2.putText(frame,f'Previous Round: {winner}',(50,300),font,1,colour,2,cv2.LINE_AA)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    #Play the game
    if startGame == False:
        cv2.putText(frame,'Press (a) to start game',org,font,1,colour,2,cv2.LINE_AA)
    if cv2.waitKey(33) == ord('a') and startGame == False:
        human_score = 0
        ai_score = 0
        gameRound = 0
        gamewinner = ''
        winner = ''
        startTime = time.time()
        startGame = True
    if startGame == True:
        currentTime = time.time() - startTime
        if int(cdTime - currentTime) > 0:
            cv2.putText(frame,f'Show hand in: {int(cdTime-currentTime)}',org,font,1,colour,2,cv2.LINE_AA)
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
                gamewinner = 'YOU WIN!'
                stopGame = False
                startGame = False
            elif ai_score == 3:
                gamewinner = 'YOU LOST!'
                stopGame = False
                startGame = False
            cv2.putText(frame,'Press (n) for next round',org,font,1,colour,2,cv2.LINE_AA)
            if cv2.waitKey(33) == ord('n'):
                startTime = time.time()
                stopGame = False
    #End of the game
    cv2.imshow('frame', frame)
    # Press q to close the window
    
            
# After the loop release the cap object
cap.release()
# Destroy all the windows
cv2.destroyAllWindows()