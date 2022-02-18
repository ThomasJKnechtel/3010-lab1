from sense_hat import SenseHat
from time import sleep
def get_sensehat():
    return SenseHat()
def alarm(sense, flash_time):
    for i in range(0,flash_time,2):
        
        sense.clear((255, 0, 0))
        sleep(1)
        sense.clear((0,0,0))
        sleep(1)
        
        