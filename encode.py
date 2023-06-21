import cv2
import face_recognition
import pickle
import os

#import all the images
folderPath = '/home/pi4/Desktop/security/knownFaces'
modePathList = os.listdir(folderPath)
imgList = []
nameList=[]
for path in modePathList:
 imgList.append(cv2.imread(os.path.join(folderPath,path)))
 nameList.append(os.path.splitext(path)[0])
 print(nameList)

#function to create all the incodings
def findEncodings(imgList):
 encodeList = []
 for img in imgList:
  img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
  encode = face_recognition.face_encodings(img)[0]
  encodeList.append(encode)

 return encodeList
print("Encoding started…")
encodeListKnown = findEncodings(imgList)
encodeListKnownWithNames = [encodeListKnown,nameList]
print("Encoding complete")

file = open("EncodeFile.p",’wb’)
pickle.dump(encodeListKnownWithNames,file)
file.close()
print("file saved")