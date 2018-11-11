import RPi.GPIO as GPIO
import time
import numpy as np;

print('Distance Measurement In Progress')

class Ultra(object):

    def setup(self):
        GPIO.setmode(GPIO.BCM)
        self.TRIG = 2
        self.ECHO = 3
        GPIO.setup(self.TRIG,GPIO.OUT)
        GPIO.setup(self.ECHO,GPIO.IN)

    def cleanup(self):
        GPIO.cleanup()

    #10次去头去尾取平均
    def get_distance(self):
        self.setup()
        distances=[]
        for i in range(10):
            GPIO.output(self.TRIG,True)
            time.sleep(0.00001)
            GPIO.output(self.TRIG,False)

            # 等待低电平结束，然后记录时间。
            while GPIO.input(self.ECHO) == 0:
                pass
            pulse_start = time.time()

            # 等待高电平结束，然后记录时间。
            while GPIO.input(self.ECHO) == 1:
                pass
            pulse_end = time.time()

            pulse_duration = pulse_end - pulse_start
            distance = pulse_duration * 17150
            distance = round(distance,2)
            distances.append(distance)
            print("Distance: {}cm".format(distance))
            time.sleep(0.0005)

        #排序=》去除两个极小值，3个极大值
        distances_np=np.array(distances)
        distances_np.sort()
        distances_np=distances_np[2:7]
        distance_mean=distances_np.sum()/5

        self.cleanup()
        return distance_mean.round(0)



if __name__=='__main__':

    GPIO.setmode(GPIO.BCM)
    TRIG = 2
    ECHO = 3
    GPIO.setup(TRIG,GPIO.OUT)
    GPIO.setup(ECHO,GPIO.IN)


    i=0
    while True:
        # 发送 self.TRIG 信号  持续 10us 的方波脉冲
        GPIO.output(TRIG,True)
        time.sleep(0.00001)
        GPIO.output(TRIG,False)


        # 等待低电平结束，然后记录时间。
        while GPIO.input(ECHO) == 0:
            pass
        pulse_start = time.time()

        # 等待高电平结束，然后记录时间。
        while GPIO.input(ECHO) == 1:
            pass
        pulse_end = time.time()


        pulse_duration = pulse_end - pulse_start
        distance = pulse_duration * 17150
        distance = round(distance,2)
        print("Distance: {}cm".format(distance))

        i+=1
        if i>600:
            # break
            pass

        time.sleep(0.05)
    GPIO.cleanup()