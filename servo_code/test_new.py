import RPi.GPIO as GPIO            # import RPi.GPIO module  
from time import sleep             # lets us have a delay  
GPIO.setmode(GPIO.BCM)             # choose BCM or BOARD  


GPIO.setup(2, GPIO.OUT) # J1
GPIO.setup(3, GPIO.OUT) # J2
GPIO.setup(4, GPIO.OUT) # J3


GPIO.setup(14, GPIO.OUT) #J4
GPIO.setup(15, GPIO.OUT) #J5
GPIO.setup(17, GPIO.OUT) #J6


GPIO.setup(18, GPIO.OUT) #J7
GPIO.setup(27, GPIO.OUT) #J8
GPIO.setup(22, GPIO.OUT) #J9

GPIO.setup(23, GPIO.OUT) #J10
GPIO.setup(24, GPIO.OUT) #J11
GPIO.setup(25, GPIO.OUT) #J2

# GPIO.output(17,1)

GPIO.output(2, 1) # J1
GPIO.output(3, 1) # J2
GPIO.output(4, 1) # J3


GPIO.output(14, 1) #J4
GPIO.output(15, 1) #J5
GPIO.output(17, 1) #J6


GPIO.output(18, 1) #J7
GPIO.output(27, 1) #J8
GPIO.output(22, 1) #J9

GPIO.output(23, 1) #J10
GPIO.output(24, 1) #J11
GPIO.output(25, 1) #J2