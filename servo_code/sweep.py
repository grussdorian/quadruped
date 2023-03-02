from gpiozero import Servo
import math
from time import sleep

from gpiozero.pins.pigpio import PiGPIOFactory

factory = PiGPIOFactory()

J1 = 2
J2 = 3
J3 = 4
J4 = 14
J5 = 15
J6 = 17
J7 = 18
J8 = 27
J9 = 22
J10 = 23
J11 = 24
J12 = 25

## Neutral positions for the following servos
J1_NEUTRAL = math.radians(-24)  
J4_NEUTRAL = math.radians(-26)
J7_NEUTRAL = math.radians(-28)
J10_NEUTRAL = math.radians(-33)

J2_NEUTRAL = 0  
J5_NEUTRAL = 0
J8_NEUTRAL = 0
J11_NEUTRAL = 0



MAX_INNER_SERVO = 0
MIN_INNER_SERVO = -50

MAX_OUTER_SERVO = 360
MIN_INNER_SERVO = 0

MIN_PULSE_WIDTH = 500/1000000
MAX_PULSE_WIDTH = 2500/1000000

servo_J1 = Servo(J1, min_pulse_width=MIN_PULSE_WIDTH, max_pulse_width=MAX_PULSE_WIDTH, pin_factory=factory)
servo_J2 = Servo(J2, min_pulse_width=MIN_PULSE_WIDTH, max_pulse_width=MAX_PULSE_WIDTH, pin_factory=factory)
servo_J3 = Servo(J3, min_pulse_width=MIN_PULSE_WIDTH, max_pulse_width=MAX_PULSE_WIDTH, pin_factory=factory)

servo_J4 = Servo(J4, min_pulse_width=MIN_PULSE_WIDTH, max_pulse_width=MAX_PULSE_WIDTH, pin_factory=factory)
servo_J5 = Servo(J5, min_pulse_width=MIN_PULSE_WIDTH, max_pulse_width=MAX_PULSE_WIDTH, pin_factory=factory)
servo_J6 = Servo(J6, min_pulse_width=MIN_PULSE_WIDTH, max_pulse_width=MAX_PULSE_WIDTH, pin_factory=factory)

servo_J7 = Servo(J7, min_pulse_width=MIN_PULSE_WIDTH, max_pulse_width=MAX_PULSE_WIDTH, pin_factory=factory)
servo_J8 = Servo(J8, min_pulse_width=MIN_PULSE_WIDTH, max_pulse_width=MAX_PULSE_WIDTH, pin_factory=factory)
servo_J9 = Servo(J9, min_pulse_width=MIN_PULSE_WIDTH, max_pulse_width=MAX_PULSE_WIDTH, pin_factory=factory)

servo_J10 = Servo(J10, min_pulse_width=MIN_PULSE_WIDTH, max_pulse_width=MAX_PULSE_WIDTH, pin_factory=factory)
servo_J11 = Servo(J11, min_pulse_width=MIN_PULSE_WIDTH, max_pulse_width=MAX_PULSE_WIDTH, pin_factory=factory)
servo_J12 = Servo(J12, min_pulse_width=MIN_PULSE_WIDTH, max_pulse_width=MAX_PULSE_WIDTH, pin_factory=factory)

servo_J1.value = math.sin(J1_NEUTRAL)
servo_J4.value = math.sin(J4_NEUTRAL)
servo_J7.value = math.sin(J7_NEUTRAL)
servo_J10.value = math.sin(J10_NEUTRAL)

try:
        while True:
            for i in range(MAX_INNER_SERVO,MIN_INNER_SERVO-1,-1):
                # servo_J3.value = math.sin(math.radians(i))
                # servo_J6.value = math.sin(math.radians(i))
                # servo_J9.value = math.sin(math.radians(i))
                # servo_J12.value = math.sin(math.radians(i))

                # servo_J2.value = math.sin(math.radians(i))
                # servo_J5.value = math.sin(math.radians(i))
                # servo_J8.value = math.sin(math.radians(i))
                # servo_J11.value = math.sin(math.radians(i))

                # servo_J1.value = math.sin(math.radians(i))   
                # servo_J4.value = math.sin(math.radians(i))
                # servo_J7.value = math.sin(math.radians(i))
                # servo_J10.value = math.sin(math.radians(i))
                sleep(0.1)


except KeyboardInterrupt:
        print("Clean exit")
        factory.close() # Prevents the servos from jumping to the previously written state immediately after powering on
