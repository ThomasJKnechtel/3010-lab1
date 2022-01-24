from sense_hat import SenseHat
import datetime
import sys
import time
import sqlite3
from time import sleep
sense = SenseHat()
sense.clear()

conn=sqlite3.connect('sensorDB.db')
c = conn.cursor()

while True:
    pressure = sense.get_pressure()
    temp = sense.get_temperature()
    humidity= sense.get_humidity()
    date = datetime.datetime.now()
    c.execute("INSERT INTO sensordata(date, temperature, humidity, pressure) VALUES(?,?,?,?)", (date, temp, humidity, pressure))
    conn.commit()
    
    sleep(1)
    