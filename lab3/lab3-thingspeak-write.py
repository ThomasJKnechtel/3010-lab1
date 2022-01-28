from sense_hat import SenseHat
from time import sleep
import requests

sendKey="Z7G9MUP9NSOUGOIQ"
url = "https://api.thingspeak.com/update"

def main():
    sense=SenseHat()
    temperature = sense.get_temperature()
    pressure = sense.get_pressure()
    humidity = sense.get_humidity()
    payload = {'field1':temperature, 'field2':pressure,'field3':humidity,'api_key':sendKey}
    while True:
        
        try:
            response = requests.get(url, params=payload)
            response=response.json()
            print(response)
        except Exception as e:
            print(e)
        sleep(120)
if __name__ == "__main__":
    main()