import time
import  RPi.GPIO as GPIO


print("init person")

class Person(object):
    def setup(self):
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(22,GPIO.IN)

    def cleanup(self):
        GPIO.cleanup()

    def check_person(self):
        self.setup()
        result=(GPIO.input(22)==False)
        print('person:{0}'.format(result))
        self.cleanup()
        return result

if __name__=='__main__':
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(22,GPIO.IN)
    i=0
    while True:
        if GPIO.input(22) == False:
            print("this is people {0}".format(i))
            i+=1
        
        time.sleep(0.1)
    print("end")
    GPIO.cleanup()

