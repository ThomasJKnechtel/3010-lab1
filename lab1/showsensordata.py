from sense_hat import SenseHat

sense = SenseHat()
sense.clear()

pressure = sense.get_pressure()
temp = sense.get_temperature()
humidity= sense.get_humidity()
sense.show_message('pressure:'+str(pressure))
sense.show_message('temperature:'+str(temp))
sense.show_message('humidity:'+str(humidity))