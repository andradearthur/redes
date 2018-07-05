import pyrebase
from pusher_push_notifications import PushNotifications

config = {
    'apiKey': "AIzaSyBpu5QxBlcfKqaIemP7XE9Ls5I0enEM0ZA",
    'authDomain': "espe-452bd.firebaseapp.com",
    'databaseURL': "https://espe-452bd.firebaseio.com",
    'projectId': "espe-452bd",
    'storageBucket': "espe-452bd.appspot.com",
    'messagingSenderId': "223433065996"
 }

firebase = pyrebase.initialize_app(config)

db = firebase.database()
pn_client = PushNotifications(
    instance_id='6211a6b6-62d9-4cc2-82de-77b831347c0d',
    secret_key='5710026DFC0CC0A41C58BD2AA9937F1',
)

def stream_handler(message):
  print(message)
  if(message['data'] is 1):
      response = pn_client.publish(
          interests=['hello'],
          publish_body={
              'apns': {
                  'aps': {
                      'alert': 'Hello!',
                  },
              },
              'fcm': {
                  'notification': {
                      'title': 'VOID ALERT',
                      'body': 'PORTA ABERTA',
                  },
              },
          },
      )

      print(response['publishId'])
my_stream = db.child("alarm1").stream(stream_handler,None)