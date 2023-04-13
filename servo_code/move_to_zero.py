from gpiozero import Servo
from time import sleep
import sys
from gpiozero.pins.pigpio import PiGPIOFactory

factory = PiGPIOFactory()

J1 = 2
J2 = 3
J3 = 20
J4 = 14
J5 = 15
J6 = 17
J7 = 18
J8 = 27
J9 = 22
J10 = 23
J11 = 24
J12 = 25

MIN_PULSE_WIDTH = 500/1000000
MAX_PULSE_WIDTH = 2500/1000000

servo = Servo(J1, min_pulse_width=MIN_PULSE_WIDTH,
                 max_pulse_width=MAX_PULSE_WIDTH, pin_factory=factory)
# servo2 = Servo(J5, min_pulse_width=MIN_PULSE_WIDTH,
#                  max_pulse_width=MAX_PULSE_WIDTH, pin_factory=factory)
mode = sys.argv[1]
if mode == "min":
    # MIN
    servo.min()
    # servo2.max()
    sleep(0.5)
    
if mode == "max":
    # MIN
    servo.max()
    # servo2.min()
    sleep(0.5)

if mode == "mid":
    # MID
    servo.mid()
    # servo2.mid()
    sleep(0.5)

print("Clean exit")
factory.close()  # Prevents the servos from jumping to the previously written state immediately after powering on
