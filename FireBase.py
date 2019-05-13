import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

import time

cred = credentials.Certificate('certificate.json')
firebase_admin.initialize_app(cred)

db = firestore.client()

ref = db.collection('data').document('Xb3HJKUG4ZKx4PPO7jyy')  
from w1thermsensor import W1ThermSensor
sensor = W1ThermSensor()

while True:
    temperature = sensor.get_temperature()
    data = {
        'temperature': temperature
    }
    ref.set(data)
    print("The temperature is %s celsius" % temperature)
    time.sleep(1)


