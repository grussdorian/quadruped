import RPi.GPIO as GPIO
from time import sleep

J3 = 4

GPIO.setmode(GPIO.BCM)
GPIO.setup(J3, GPIO.OUT)
# GPIO.setup(18,GPIO.OUT)
# GPIO.setup(25, GPIO.OUT)
pwm=GPIO.PWM(J3, 50)
# pwm2=GPIO.PWM(18,50)
# pwm3 = GPIO.PWM(25, 50)
pwm.start(0)
# pwm2.start(0)
# pwm3.start(0)

pwm.ChangeDutyCycle(3) # left -90 deg position
# pwm2.ChangeDutyCycle(3)
# pwm3.ChangeDutyCycle(3)

sleep(1)

pwm.ChangeDutyCycle(1.5) # left -90 deg position
# pwm2.ChangeDutyCycle(1.5)
# pwm3.ChangeDutyCycle(1.5)
sleep(1)


# pwm.ChangeDutyCycle(7.5) # neutral position
# sleep(1)
# pwm.ChangeDutyCycle(10) # right +90 deg position
# sleep(1)

pwm.stop()
GPIO.cleanup()
'''
import RPi.GPIO as GPIO 
from time import sleep 
GPIO.setwarnings(False) 
 
GPIO.setmode(GPIO.BCM) 
GPIO.setup(17, GPIO.OUT) 
 
while True: 
    GPIO.output(17, True) 
    sleep(1) 
    GPIO.output(17, False) 
    sleep(1)
'''
