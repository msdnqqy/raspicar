import RPi.GPIO as GPIO
import time
class Rotation:
    frequency=50
    delta_theta=0.2
    min_delay=0.0006
    max_delay=0.4

    def __init__(self,channel,min_theta,max_theta,init_theta=0):
        
        self.channel=channel 
        if(min_theta<0 or min_theta>180):
            self.min_theta=0
        else:
            self.min_theta=min_theta
        if(max_theta<0 or max_theta>180):
            self.max_theta=180
        else:
            self.max_theta=max_theta
            if(init_theta<min_theta or init_theta>max_theta):
                self.init_theta=(self.min_theta+self.max_theta)/2
            else:
                self.init_theta=init_theta
        self.min_dutycycle=2.5+self.min_theta*10/180
        self.max_dutycycle=2.5+self.max_theta*10/180


    def setup(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(self.channel,GPIO.OUT)
        self.pwm=GPIO.PWM(self.channel,Rotation.frequency)
        self.dutycycle=2.5+self.init_theta*10/180
        self.pwm.start(self.dutycycle) 
        time.sleep(Rotation.max_delay)

    def positiveRotation(self):
        self.dutycycle=self.dutycycle+Rotation.delta_theta*10/180
        if self.dutycycle>self.max_dutycycle:
            self.dutycycle=self.max_dutycycle
        self.pwm.ChangeDutyCycle(self.dutycycle)
        time.sleep(Rotation.min_delay)

    def reverseRotation(self):
        self.dutycycle=self.dutycycle-Rotation.delta_theta*10/180
        if self.dutycycle<self.min_dutycycle:
            self.dutycycle=self.min_dutycycle
        self.pwm.ChangeDutyCycle(self.dutycycle)
        time.sleep(Rotation.min_delay)

    def specifyRotation(self,theta): 
        if(theta<0 or theta>180):
            return
        self.dutycycle=2.5+theta*10/180
        self.pwm.ChangeDutyCycle(self.dutycycle)
        time.sleep(Rotation.max_delay)

    def cleanup(self):
        self.pwm.stop()
        time.sleep(Rotation.min_delay)
        GPIO.cleanup()


if __name__=='__main__':

    hRotation=Rotation(12,0,180,0)
    hRotation.setup()
    for i in range(10):
        hRotation.positiveRotation()
        time.sleep(0.1)

    for i in range(10):
        hRotation.reverseRotation()
        time.sleep(0.1)

    hRotation.cleanup()