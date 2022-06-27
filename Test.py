from statistics import mode
import cv2
from keras.models import load_model
import numpy as np
import time
model = load_model('keras_model.h5')
cap = cv2.VideoCapture(0)
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
cdTime = float(4.0)
startTime = time.time()
while (time.time() - startTime) < cdTime:
    print(int(time.time()-startTime))
    ret, frame = cap.read()
    resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
    image_np = np.array(resized_frame)
    normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
    data[0] = normalized_image
    prediction = model.predict(data)

    if prediction[0][0] > 0.5:
        print('Rock')
    elif prediction[0][1] > 0.5:
        print('Paper')
    elif prediction[0][2] > 0.5:
        print('Scissors')
    else:
        print('Nothing')
    
    cv2.imshow('frame', frame)
    # Press q to close the window
    #print(prediction)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
            
# After the loop release the cap object
cap.release()
# Destroy all the windows
cv2.destroyAllWindows()