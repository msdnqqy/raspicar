import sys
import RPi.GPIO as GPIO
import time
print('init Car')

class Car(object):
    def __init__(self):
        self.port=[11,12,13,15,16,18]
        self.diretionPower={'up':[GPIO.HIGH,GPIO.LOW,GPIO.HIGH,GPIO.LOW],
                            'down':[GPIO.LOW,GPIO.HIGH,GPIO.LOW,GPIO.HIGH],
                            'left':[False,False,GPIO.HIGH,GPIO.LOW],
                            'right':[GPIO.HIGH,GPIO.LOW,False,False]}

    def init(self):
        GPIO.setmode(GPIO.BOARD)
        for i in range(6):
            GPIO.setup(self.port[i],GPIO.OUT)
        
    def run(self,diretion,sleeptime):
        self.init()
        power=self.diretionPower[diretion]
        for i in range(4):
            GPIO.output(self.port[i],power[i])

        pwm1=GPIO.PWM(16,80)
        pwm2=GPIO.PWM(18,80)
        pwm1.start(30)
        pwm2.start(30)
        time.sleep(sleeptime)
        pwm1.stop()
        pwm2.stop()
        GPIO.cleanup()