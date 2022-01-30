import pyrebase
import random
import time
from datetime import datetime
from sense_hat import SenseHat
# Create new Firebase config and database object


# Write random numbers to database
def writeData():
  sense=SenseHat()
  config = {
      "apiKey": "AIzaSyBofg5etl3l8QQz9EPUIaMHH-0RsKkFvNw",
      "authDomain": "lab3-1d7f0.firebaseapp.com",
      "databaseURL": "https://lab3-1d7f0-default-rtdb.firebaseio.com/",
      "storageBucket": "lab3-1d7f0.appspot.com"
    }

  firebase = pyrebase.initialize_app(config)
  db = firebase.database()
  dataset = "SensorData"
  temp = sense.get_temperature()
  humidity=sense.get_humidity()
  pressure=sense.get_pressure()
  key=0
  while True:
    # I'm using dummy sensor data here, you could use your senseHAT
    sensorData = {"temperature":temp, "pressure":pressure, "humidity":humidity}

    # Will be written in this form:
    # {
    #   "sensor1" : {
    #     "0" : 0.6336863763908736,
    #     "1" : 0.33321038818190285,
    #     "2" : 0.6069185320998802,
    #     "3" : 0.470459178006184,
    #   }
    # }
    # Each 'child' is a JSON key:value pair
   
    db.child(dataset).child(key).set(sensorData)
    
    key=key+1
    time.sleep(1)

def readData():
  # Returns the entry as an ordered dictionary (parsed from json)
  config = {
  "apiKey": "AIzaSyB34rNm8y69gJmrme-6kaWNiYtdAsbIzLs",
  "authDomain": "sysc3010lab3-97b95.firebaseapp.com",
  "databaseURL": "https://sysc3010lab3-97b95-default-rtdb.firebaseio.com/",
  "storageBucket": "sysc3010lab3-97b95.appspot.com"
}
  firebase = pyrebase.initialize_app(config)
  db = firebase.database()
  dataset = "Lab3"
  mySensorData = db.child(dataset).get()

 
  # Returns the dictionary as a list
  mySensorData_list = mySensorData.each()
  # Takes the last element of the list
  dataLength =len(mySensorData_list)
  for i in range(dataLength-3, dataLength):
      print("Child Key: {}".format(mySensorData_list[i].key()))
      print("Child Value: {}\n".format(mySensorData_list[i].val()))

