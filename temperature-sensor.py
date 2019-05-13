import time
import requests
import json
URL = "http://ec2-3-86-210-188.compute-1.amazonaws.com:8090/temperature"
  
from w1thermsensor import W1ThermSensor
sensor = W1ThermSensor()
head = {'Content-type': 'application/json'}

while True:
    temperature = sensor.get_temperature()
    PARAMS = {'temp': "%s" % temperature}
    #PARAMS = {'temp': '36'}
    #print(PARAMS)
    #resp = requests.post(url = URL, data = json.dumps(PARAMS), headers = head) 
    #print(resp.text)
    print("The temperature is %s celsius" % temperature)
    time.sleep(1)
