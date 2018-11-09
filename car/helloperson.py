import time
import  RPi.GPIO as GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(22,GPIO.IN)

print("begin")
i=0
while True:
    if GPIO.input(22) == False:
        print("this is people {0}".format(i))
        i+=1
    
    time.sleep(0.1)
print("end")
GPIO.cleanup()