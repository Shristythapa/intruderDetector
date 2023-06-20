#import the necessary packages
from imutils.video import VideoStream
from imutils.video import FPS
import face_recognition
import imutils
import pickle
import time
import cv2
import numpy as np


#load the encoding file
print("Loading encode file..")
file = open('EncodeFile.p','rb')
encodeListKnownWithNames = pickle.load(file)
file.close()
encodeListKnown,nameList = encodeListKnownWithNames
#print(nameList)
print("Encode file loaded")

#store results
detection=False
person=None

vs = VideoStream(usePiCamera=True).start()
time.sleep(2.0)

# start the FPS counter
fps = FPS().start()


while True:
    img = vs.read()
    img = imutils.resize(img, width=500)
   

     
    #find location faces in the current frame 
    faceCurrFrame = face_recognition.face_locations(img)
    
    #create encodings of the faces detected
    encodeCurrFrame = face_recognition.face_encodings(img, faceCurrFrame)#provide location of the face in the image and the image
    

    
    #loop through all the encoding and generate outcome according to wether they match or not
    #using zip cause we want to use for loop of two variable
    for encodeFace, faceLoc in zip(encodeCurrFrame,faceCurrFrame):
        
        #compare encodeface unknown to encodeface known
        matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
        
        #the lower the distance the better the match
        faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)
        
       #true and false for all the images in the known dir
#         print("Matched",matches)
        
#         print("Face Distance",faceDis)
        
    #getting the index of the least value
        matchIndex = np.argmin(faceDis)
       # print(type(faceDis[matchIndex]))
#         print("Match Index", matchIndex)
        
        if matches[matchIndex]:
            detection="Known Face Detected"
            person=nameList[matchIndex]
            
            y1,x2,y2,x1 = faceLoc
            y1,x2,y2,x1= y1*4,x2*4,y2*4,x1*4
            #draw the rectangle accross the face
            cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
        else:
          detection="No face detected"
           
#             # Add a label with the name of the person, or "Unknown" if their name is not recognized
#         face_image = img[y1:y2, x1:x2]
#         face_encodings = face_recognition.face_encodings(imgS, [faceCurrFrame])[0]
#       # Here you would add code to recognize the person in the face image, and retrieve their name
#     # For this example, we'll just use "Unknown"
#         label = nameList[matchIndex]
#         cv2.putText(image, label, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_DUPLEX, 0.5, (0, 255, 0), 1)

            
            
        
            
             
     # display the image to our screen
    cv2.imshow("Facial Recognition is Running", img)
    key = cv2.waitKey(1) & 0xFF           
   

    if cv2.waitKey(20) & 0xFF == ord('q'):
        print("Status: {}".format(detection))
        print("Person: {}".format(person))
        break
        
# update the FPS counter
    fps.update()

# stop the timer and display FPS information
fps.stop()
print("[INFO] elasped time: {:.2f}".format(fps.elapsed()))
print("[INFO] approx. FPS: {:.2f}".format(fps.fps()))

# do a bit of cleanup
cv2.destroyAllWindows()
vs.stop()
