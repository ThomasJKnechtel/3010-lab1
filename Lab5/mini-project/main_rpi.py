from helper_functions import camera, computer_vision,sensehat
from time import sleep

def main():
    camera_i = camera.get_camera() #DO NOT MODIFY, function call must work as is 
    sense = sensehat.get_sensehat() #DO NOT MODIFY, function call must work as is 
    
    userinput = input("Enter '2' to take the background image else press different key")
    take_background_image=False
    if userinput == "2":
        take_background_image = True #TO-DO: Should be a user input

    if take_background_image:
        print("get out of the scene picture taken in 10 sec")
        for i in range(10):
            sleep(1)
            print(10-i)
            
        preview = False
        countdown=0
        camera.capture_image(camera_i,"data/images/background.jpg", countdown_time=countdown, preview=preview) #DO NOT MODIFY, function call must work as is 
    
    arm_system = False #TO-DO: Should be a user input
    userinput = input("would you like to arm the system? y/n")
    if userinput=='y':
        arm_system=True
    if arm_system:
        interval = int(input("Enter the interval between test images in seconds:"))
        t1 = int(input("Enter the threshold t1: "))
        
        print("Monitoring will begin in 10 seconds...")
        for i in range(10):
            sleep(1)
            print(10-i)

        count = 0
        while True: #DO NOT MODIFY, function call must work as is 
            camera.capture_image(camera_i,"data/images/image%s.jpg" % count, countdown_time=interval) #DO NOT MODIFY, function call must work as is 
            person_detected = computer_vision.person_detected("data/images/background.jpg","data/images/image%s.jpg" % count, t1)  #DO NOT MODIFY, function call must work as is 
            if person_detected: #DO NOT MODIFY, function call must work as is 
                print("Person Detected") #DO NOT MODIFY, function call must work as is 
                sensehat.alarm(sense,interval)  #DO NOT MODIFY, function call must work as is 
            else:
                print("No Person Detected") #DO NOT MODIFY, function call must work as is 
            count += 1


if __name__ == "__main__":
    main()
