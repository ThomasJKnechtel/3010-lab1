# Lab 3 Internet of Things
  The focus of this lab was interacting with cloud databases using Thingspeak and Firespace
## lab3-thingspeak-read.py [https://github.com/ThomasJKnechtel/SYSC3010_Thomas_Knechtel/blob/master/lab3/lab3-thingspeak-read.py]
  This program sends a GET read request to a teamates thingspeak database and prints out the temperature, presssure and humidity stored in the database on the SenseHat
## lab3-thingspeak-write.py [https://github.com/ThomasJKnechtel/SYSC3010_Thomas_Knechtel/blob/master/lab3/lab3-thingspeak-write.py]
  This program sends a HTTP GET write request to my thingspeak databse and writes the sensors temperature, pressure and humidity from the SenseHat every 2 minutes.
## lab3-firespace.py [https://github.com/ThomasJKnechtel/SYSC3010_Thomas_Knechtel/blob/master/lab3/lab3-firespace.py]
  ### writeData()
    Writes the temperature, pressure and humidity to my Firespace database and stores the data in a table called SenseData
  ### readData()
    prints the last 3 datapoints stored in a teammates Firespace database.
