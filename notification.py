import firebase_admin
from firebase_admin import credentials, messaging

cred = credentials.Certificate("/home/pi4/Desktop/security/security.json")
firebase_admin.initialize_app(cred)

def send_notification(token, title, body):
  message = messaging.Message(
   notification=messaging.Notification(
    title=title,
    body=body
    ),
   token=token
 )
  response = messaging.send(message)
  print('Notification sent successfully:', response)
 
token = 'ccUGWT-OSlCM3Lq2gkWRgC:APA91bEOJ-kU3ujZEUPjtzYf90Lk74S0MmcINZvkXeOTWisMmSSMRn7Odc7mlTRvLwAGBdX-hPOygeDqSIhSzRXEd423MGhsiTrmtaQE7Xk557mHSZuBvV60r6qRcsXNjxG1lqCmIpN7'
title = 'Notification Title'
body = 'Notification Body'
send_notification(token, title, body) 