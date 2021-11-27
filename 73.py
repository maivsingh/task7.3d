import RPi.GPIO as GPIO       
import time
GPIO.setmode(GPIO.BCM)         
GPIO.setup(Led, GPIO.OUT)      
GPIO.setup(trigger, GPIO.OUT)  
GPIO.setup(echo, GPIO.IN)     

Led = 21                      
trigger = 18                
echo = 24                    


pwm = GPIO.PWM(Led, 100)       
pwm.start(0)                   

def dist():
    GPIO.output(trigger, True) 
    time.sleep(0.00001)
    GPIO.output(trigger, False)

    Start = time.time()
    Stop = time.time()
    while GPIO.input(echo) == 0:
        Start = time.time()
    while GPIO.input(echo) == 1:
        Stop = time.time()
    TimeElapsed = Stop - Start
    dist = (TimeElapsed * 34300) / 2

    return distance

try:
    while 1:                  
        dist = dist()
        print ("dist = %.1f cm" % dist) 
        if (dist > 400):       
            x = 0              
        else:
            x = 100 - (dist / 4) 
        pwm.ChangeDutyCycle(x)
        time.sleep(0.01)        

except KeyboardInterrupt:
    pass      
pwm.stop()     
GPIO.cleanup() 
