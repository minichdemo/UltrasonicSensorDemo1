import RPi.GPIO as GPIO
import time
import os

 
#GPIO Mode (BOARD / BCM)
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
#set GPIO Pins
GPIO_TRIGGER = 18
GPIO_ECHO = 24
 #set GPIO direction (IN / OUT)
GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)
GPIO.setup(4,GPIO.OUT)
GPIO.setup(23, GPIO.OUT)
GPIO.setup(17, GPIO.OUT)
def distance():
    # set Trigger to HIGH
    GPIO.output(GPIO_TRIGGER, True)
 
    # set Trigger after 0.01ms to LOW
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)
 
    StartTime = time.time()
    StopTime = time.time()
 
    # save StartTime
    while GPIO.input(GPIO_ECHO) == 0:
        StartTime = time.time()
 
    # save time of arrival
    while GPIO.input(GPIO_ECHO) == 1:
        StopTime = time.time()
 
    # time difference between start and arrival
    TimeElapsed = StopTime - StartTime
    # multiply with the sonic speed (34300 cm/s)
    # and divide by 2, because there and back
    distance = (TimeElapsed * 34300) / 2
 
    return distance
 
if __name__ == '__main__':
    try:
        while True:
            GPIO.output(17,GPIO.LOW)
            GPIO.output(4,GPIO.LOW)
            GPIO.output(23,GPIO.HIGH)
            dist = distance()
            print ("Measured Distance = %.1f cm" % dist)
            time.sleep(1)
            # blue LED flash when within 10cm
            if dist < 10:
                GPIO.output(17,GPIO.HIGH)
                time.sleep(0.3)
            # red LED long and picture taken when within 5cm
            if dist < 5:
                GPIO.output(4,GPIO.HIGH)
                print("detect")
                os.system('camerajack.sh')
                #time.sleep(5)
            '''
            if dist < 7:
                print("detect")
                run_once = 0
                while 1:
                    if run_once == 0:
                        os.system('camerajack.sh')
                        run_once = 1
            '''
        # Reset by pressing CTRL + C
    except KeyboardInterrupt:
        print("Measurement stopped by User")
        GPIO.output(23,GPIO.LOW)
        GPIO.output(4,GPIO.LOW)
        GPIO.output(17, GPIO.LOW)
        GPIO.cleanup()
        

