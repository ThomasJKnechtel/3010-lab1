import requests
from sense_hat import SenseHat
readKey = "8BMQ68D2C14CSVUD"
channel_Number = "1640845"
url ="https://api.thingspeak.com/channels/"+channel_Number+"/feeds.json"
results = 2
def main():
    payload = {'api_key':readKey, 'results':results}
    response=requests.get(url, params=payload)
    response=response.json()
    print("Channel name: {}".format(response['channel'],['name']))
    entries = response['feeds']
    sense = SenseHat()
    sense.clear()
    for e in entries:
        try:
            sense.show_message("temperature: "+e['field1'])
            sense.show_message("pressure : "+e['field2'])
            sense.show_message("humidity : " +e['field3'])
        except TypeError:
            sense.show_message("Null Value")
if __name__=="__main__":
    main()
    