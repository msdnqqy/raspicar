import sys
import RPi.GPIO as GPIO
import time
import tornado.ioloop
import tornado.web
import tornado.httpserver
import tornado.options
from hellopower import Rotation
from helloultra import Ultra
from hellocar import Car

from tornado.options import define,options
define("port",default=80,type=int)

# port=[11,12,13,15,16,18]
# diretionPower={'up':[GPIO.HIGH,GPIO.LOW,GPIO.HIGH,GPIO.LOW],
#                     'down':[GPIO.LOW,GPIO.HIGH,GPIO.LOW,GPIO.HIGH],
#                     'left':[False,False,GPIO.HIGH,GPIO.LOW],
#                     'right':[GPIO.HIGH,GPIO.LOW,False,False]}

# def init():
#     GPIO.setmode(GPIO.BOARD)
#     for i in range(6):
#         GPIO.setup(port[i],GPIO.OUT)
    
# def run(diretion,sleeptime):
#     init()
#     power=diretionPower[diretion]
#     for i in range(4):
#         GPIO.output(port[i],power[i])

#     pwm1=GPIO.PWM(16,80)
#     pwm2=GPIO.PWM(18,80)
#     pwm1.start(50)
#     pwm2.start(50)
#     time.sleep(sleeptime)
#     pwm1.stop()
#     pwm2.stop()
#     GPIO.cleanup()


class IndexHandler(tornado.web.RequestHandler):
    hRotation=Rotation(12,0,180,0)

    def get(self):
        self.render("index.html")
    
    def post(self):
        sleeptime=0.1
        arg=self.get_argument('k')

        result="return param:"+arg

        car=Car()
        if arg=='w':
            car.run('up',sleeptime)
        elif arg=='s':
            car.run('down',sleeptime)
        elif arg=='a':
            car.run('left',sleeptime)
        elif arg=='d':
            car.run('right',sleeptime)

        elif arg=='q':
            hRotation=Rotation(12,0,30,0)
            hRotation.setup()
            hRotation.positiveRotation()
            hRotation.cleanup()
        elif arg=='e':
            hRotation=Rotation(12,0,30,0)
            hRotation.setup()
            hRotation.reverseRotation()
            hRotation.cleanup()

        elif arg=='r':
            ultra=Ultra()
            distance=ultra.get_distance()
            result="{0}".format(distance)
        
        print(result)
        self.write(result)

if __name__=='__main__':
    tornado.options.parse_command_line()
    app=tornado.web.Application(handlers=[(r"/",IndexHandler)])
    http_server=tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()

