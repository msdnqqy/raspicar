import RPi.GPIO as GPIO
import time

port=[11,12,13,15]
diretionPower={'up':[GPIO.HIGH,GPIO.LOW,GPIO.HIGH,GPIO.LOW],
                    'down':[GPIO.LOW,GPIO.HIGH,GPIO.LOW,GPIO.HIGH],
                    'left':[False,False,GPIO.HIGH,GPIO.LOW],
                    'right':[GPIO.HIGH,GPIO.LOW,False,False]}

def init():
    GPIO.setmode(GPIO.BOARD)
    for i in range(4):
        GPIO.setup(port[i],GPIO.OUT)
    
def run(diretion,sleeptime):
    init()
    power=diretionPower[diretion]
    for i in range(4):
        GPIO.output(port[i],power[i])
    
    time.sleep(sleeptime)
    GPIO.cleanup()

if __name__=='__main__':
    print("begin---")
    run('up',1)
    run('down',1)
    run('left',1)
    run('right',1)
    print('end---')

