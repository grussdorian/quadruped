# Documentation for Pupper

1. [Parts sourcing](#1-parts-sourcing)
2. [Assembly](#2-assembly)
3. [Connections](#3-connections)
4. [Code](#4-code)
5. [Calibration](#5-calibration)
6. [Running the robot](#6-running-the-robot)
7. [Controlling](#7-controlling)
8. [Things which are still left](#8-things-to-do)
9. [Checklist of things before connecting the PCB to the RPi](#9-checklist-of-things-which-are-needed-before-connecting-the-pcb-to-the-raspberry-pi)

## 1. Parts sourcing.

Please refer to [This spreadsheet](https://docs.google.com/spreadsheets/d/1AzzCM8UDrbhDfgtIsiQplI5SMlo7OLG8/edit#gid=1202520655). Part sourcing is listed here comprehensively.

For building the quadruped's body and legs, we have used 5mm fibre sheets. Ideally it should be carbon fibre. But we could not find a vendor who could cut the carbon fibre sheets according to our specifications. Also laser cutting of carbon fibre is not possible in the lab. The next best choice was to use acrylic fibre and that is what we used. $3$ mm thickness for legs and $5$ mm thickness for the base and top.

All the structural elements are taken from [here](https://a360.co/2TEh4gQ)
[![Pupper](/img/Pupper.png "Codey the Codecademy mascot")](https://stanford195.autodesk360.com/g/shares/SH919a0QTf3c32634dcfedf61e031f673710)

### Laser Cut parts

| Part name                 | Quantity | Thickness (mm) |
| ------------------------- | -------- | -------------- |
| Acrylic fibre plate top   | 1        | 5              |
| Acrylic fibre plate bottm | 1        | 5              |
| Lower leg                 | 4        | 3              |
| Upper leg                 | 4        | 3              |

To obtain the design of the above parts, we extracted each of the above mentioned prefab from the fusion 360 model. For laser cutting, we had to project the legs, and the base on a 2d surface in fusion, and extract the traces. Then we used laser cad for some final retouching.

_Note:_ The design provided here has two holes in the upper legs, both of them are useless as they do not fit our servo horn. So we had to modify the position of the hole in laser CAD to be $0.85$ mm from the beginning of the curvature. **Update:** We have used mild steel to make the legs, as the acrylic legs could not handle the heavy weight of the robot

_Update_ The design of the upper leg has been modified and now we are not using the plastic disc to prevent slipping. Instead we have prototyped (with acrylic) a leg with two holes which fit perfectly in the two holes of the leg. [We are going to laser cut it in aluminum.](#8-things-to-do)

![Upper Leg](/img/Upper%20leg.png)

### 3D printed parts

_Note that the 3D printed parts had holes much bigger than the size of the inserts. So the inserts did not fit in the holes. Instead we tried to use nuts and washers to tighten the screws where the inserts would have gone_

For the 3D printed Structures, we used PLA or PETG, 0.2mm-0.4mm layer height, >50% infill.

| Part name               | STL name          | Quantity |
| ----------------------- | ----------------- | -------- |
| Body support - "Front1" | FrontFront.stl    | 1        |
| Body support - "Front2" | FrontBack.stl     | 1        |
| Body support - "Back1"  | BackFront.stl     | 1        |
| Body support - "Back2"  | BackBack.stl      | 1        |
| Inner Hip               | HipInsideFDM.stl  | 4        |
| Outer Hip               | HipOutsideFDM.stl | 4        |

All the parts are uploaded in the [3D printed files](/3DPrintedFiles/)

After all the raw materials and parts are available, we can move to assembly

### PCB

![PCB](/img/pcb.png) required to power all the servos, provide signal from the Raspberry Pi. It sits on top of the GPIO pins of the Pi. It can also be used to power the Pi [something we messed up doing](#what-went-wrong).
The [Gerber files](https://github.com/stanfordroboticsclub/Pupper-Raspi-PDB/) could be used to print the PCB using any standard PCB manufacturer. _NOTE_ 2 oz copper should be used for the traces. After getting the PCB, we need to solder the headers as shown in the image. Solder a pigtail connector wire in J13 to connect the battery. Make sure that the pigtail wire is joined above (side facing the male headers) the PCB. Solder the female $20\times2$ female header on the back side of the PCB.

**Update** There was jittering, (i.e incorrect pwm signals) in for J3. So we had to cut out the header for the signal pin of J3 and attach a jumper wire from GPIO pin `20` to signal socket of J3 directly. In future PCBs This change is to be [incorporated](#8-things-to-do)

## 2. Assembly

Pupper has 4 legs, each with 3 sets of [servos](https://robokits.co.in/motors/rc-servo-motor/ultra-torque-metal-gear-35kgcm-coreless-stainless-steel-pinion-standard-servo-motor). These servos are placed inside 3D printed hip joints.

### All reference images are placed under folder [img](/img)

![Servo placement and numbering](/img/body7com.jpg)

### Hip assembly

All the servos should be housed inside hip joints in the following way:

1. First, screw metallic disc with $J1,J4,J7,J10$. _Important_: apply some hot glue after fixing the disc tightly with the servo.

2. Take inner hip and screw 4 black m4x6 screws that came with the servos to the disc.

3. Place $J2,J5,J8,J11$ in the inner hip and use m3x20 screws to tighten the side of the hip facing away from the disc.

4. _Note:_ Tightening should be enough such that the screw pokes out from the other side of the inner hip. Here we need to fasten the 20mm spacers. Tighten the servo with m3x10 screws (for the remaining two holes)

_Choice of the screw is important. The horn should be facing away from the 4 spacers and should be able to rotate freely without any obstruction. So the screws should be tightened upto that extent only which does not cause any obstruction in the horn's way_

5. Place the other set of 20mm spacers on the screws fastened on the sideof the plastic case, i.e they do not tighten the servo.

   Then the plastic disc that came with the servos should be attached ring side facing up, to $J5,J2,J8,J11$ along with 25T servo horn beneath the disc (which came with the servos as well).

_The disc is used to create spacing for the legs. It makes sure that the legs don't slip while rotating._

6. Attach 25T horn to $J3,J6,J9,J12$. This horn should parallel to the other set of horns i.e $J5,J2,J8,J11$ and should face the free side of the enclosure.

### Leg assembly

Take the laser cut parts, upper legs and lower legs and place a thrust bearing between the two joints, and another bearing to the side of the screw head. The flat end of the lower leg should touch the ground and the lower leg should be facing outwards, away from the body. Place a m3x16 screw between the sandwitched joints and tighten a nylon locknut from the other end. This way prepare all the 4 legs.

![hip6](/img/hip6preright.jpg)

Connect the upper legs to $J5,J2,J8,J11$, with a m3x10 screw. The curvature of the upper leg should fit just right in the disc. The disc is there to prevent the le from slipping.

### Muscles

After legs have been attached to the servos, take two ball joints and tighten a threaded piece of metal between two ball joints. The length from one hole to another hole should be exactly $123.5$ mm, for all 4 sets of muscles.

![hip13](/img/hip13com.jpg)

Connect the four muscles with a m3x8 screw to the horns of the servos $J3,J6,J9,J12$. Connect the other end to the hole made in the extreme upper part of the lower leg.

All 4 legs are ready now.

### Body assembly

Take the laser cut base of the body and put all the 3D printed structure on the corresponding place. Take m3x16 screws and a washer. Put the washer on the plastic and screw to the other end. Fasten the screw with a normal locknut.

Place all the plastic parts and tighten them to the base of the body. Now place $J1,J4,J7,J10$ in their respective positions and tighten them with screws. All the legs are now attached to the body.

Now we can proceed to wiring and after than we would need to attach the upper part of the body.

## 3. Connections

$$
  yellow \rightarrow signal
$$

$$
  red \rightarrow power
$$

$$
  brown \rightarrow ground
$$

All the servos should be connected to the [PCB](https://github.com/stanfordroboticsclub/Pupper-Raspi-PDB/), which is connected to the Raspberry Pi. The PCB is well marked and the signal side of the connector should face the GPIO headers.

![Connection](/img/body7pre.jpg)
The pigtail connector (Big wire on the right) is connected to the battery powering 7.4 volts and that power is converted to 5 volts using a voltage converter on the left. The output of the voltage converter _should_ be 5 Volts which directly plugs in our PCB where it is marked +5 volts and ground.

## What went wrong

Never try to power the RPi with anything less than 4.75 volts and 5.25 volts. This was the mistake which costed us our Raspberry Pi 3 model B plus.
I tested the output of the voltage converter, which showed 5 volts and I powered on the Raspberry Pi. It turned on and I SSHed into the Pi. Tested one servo and it was all good. Then I turned off the RPi using shutdown command from SSH.

However next time before turning on the RPi I did not check the voltage and it didn't turn on. I quickly unplugged the battery and then disconnected the board. Later when I was testing the voltage converter separately, the output of the voltage converter was same as the input with some voltage drop i.e it was showing 6.8 volts!

Assuming our worst fear, I waited for another day and checked online forums whether the RPi has polyfuse or not. It turns out that the Raspberry Pi has polyfuse, but they are placed between the input and the SOC so the GPIO side where we plugged in our power supply had no protection.

I double checked all the [testing points](https://ozzmaker.com/testing-points-raspberry-pi/) in the Pi and confirmed that the raspberry pi has indeed been shorted.

**NOTE** Always check the power supply before plugging into the Pi. Since it is powered by micro USB we might be tempted to power it on from our computer's USB port but **DON'T** do that as that port can never provide enough current to the board. Similarly always check for faulty power supply and voltage levels before powering on the Pi.

## 4. Code

Code for the quadruped has been taken from the open source project by Stanford robotics group [here](https://github.com/stanfordroboticsclub/StanfordQuadruped) and the joystick controller code has been taken from [here](https://github.com/stanfordroboticsclub/PS4Joystick). The code is very well documented and self explanatory but it had an [issue](#added-wireddongle-controller-support)

I did not use the image they provided for flashing the SD card. The image is way to old and I faced many problems while updating repositories. Thus I ended up using a standard 32 bit distribution of [Raspbian](https://www.raspberrypi.com/software/operating-systems/#raspberry-pi-os-32-bit).

After etching the SD card with [Raspberry Pi's image software](https://www.raspberrypi.com/software/) I booted into the Pi.

Raspbian provides a GUI so our job was easier. Later the plan was to remove the Desktop Environment and only keep the CLI to reduce system overhead.
With the pi connected to USB mouse, keyboard and a display, we set up wifi on the pi so we could use it in headless mode in the future. All successive accesses were made using VNC or SSH. And the pi was only connected to power using a wall adapter which supported 3A 5V.

### Added wired/dongle controller support

The default code They provided had only support for a PS4 Dualshock controller. And not only that, the internal code for the working of the robot, is also very much intertwined with the proprietary code it shipped with. Thus I had to rewrite the code to add support for wired / standard bluetooth controller with a dongle like the Logitech f710 controller we used. ![controller](/img/controller.jpg)

The modified code is [here](https://github.com/grussdorian/PupperCommand) and [here](https://github.com/grussdorian/pupper)

### What were the changes?

Dualshock 4 uses a proprietary protocol to communicate to the bluetooth connected device. The Python package to parse the input stream is also hacky and reverse engineered. Dualshock 4 is also very expensive. So adding support for generic X-input supported controllers were a requirement.

The data buffer sent received by the Python package is a dictionary

```python
input_buff = {
"LS":0.6501,
"RS":-0.1304,
"x":1,
"triangle":0,
"square":1,
"circle":1,
"L1": 1
"L2": 0.2452
....
}
```

The values may not be normalised but float values $\in [-128,127]$. So they were normalised between -1 to 1.
Then the UDP connection objects that were communicating with the controller were deleted.

The connection to the controller part has been completely re-written. It still uses UDP but the events fired by the UDP publisher object is interrupt driven (from the usb). Thus, this is more efficient in terms of polling in regular intervals (which dualshock 4 was doing). The only caveat is now the publisher has to publish in two different ports, one for activating the robot and another for driving the robot, while the first one listens for shutdown command.
This is a quick way of doing things but I will soon change the code to only publish to one port.

## 5. Calibration

To calibrate the servos, first we need to set the servo to its neutral position without the horns, then test whether they can move freely (whether addition of the horns would create an obstruction in the path of the servo).

To do this, first we need to plug in the servo individually to the PCB and power on the Raspberry Pi. If `robot.service` is running, first stop it by `sudo systemctl stop robot.service`. Then cd to the directory `servo_code/quadruped/servo_code/` and modify the file `move_to_zero.py` with the servo which we are currently trying to move.

`move_to_zero.py` Takes two command line arguments:-

1. min
2. max

i.e

```console
pupper@pupper cd servo_code/quadruped/servo_code/
pupper@pupper/servo_code/quadruped/servo_code/ python3 move_to_zero.py min
```

would move the servo which is currently being selected in the code.

Change the part of the code as:

```python
servo_JXX = Servo(JXX, min_pulse_width=MIN_PULSE_WIDTH,
                 max_pulse_width=MAX_PULSE_WIDTH, pin_factory=factory)
```

Change X with the number of servo you want to move to min or max

i.e

```python
servo_J10 = Servo(J10, min_pulse_width=MIN_PULSE_WIDTH,
                 max_pulse_width=MAX_PULSE_WIDTH, pin_factory=factory)
```

Then run the code:

```console
pupper@pupper/servo_code/quadruped/servo_code/ python3 move_to_zero.py min
```

To move the servo to its min position. Accordingly place the hip joints **only after making sure that there is no obstruction**

**Note if the horn gets stuck, it can potentially damage the servo and widen the dead-zone for the servo. (Which means without putting any load on the servo, it would wobble every so slightly. This wobble might increase when the horn is stuck and the servo is trying its best to push it against the metal standoffs, acrylic body or the plastic frame)**

The correct alignment of the horns is as follows:

![controller](/img/zero_position_alignment_servo_horn.png)

Note that the horns are just barely touching the metal standoffs. For the inner hip (servo behind) the horn is at its max. The servo in the front is at its min. This position is chosen such that when the leg tries to adjust every time when the following calibration code is run, or when the robot is [activated using the controller](#6-running-the-robot), the default position is such that nothing gets obstructed.

Earlier the horns were vertical, which was creating obstruction when the robot was [being activated](#6-running-the-robot). It had to be taken to the walking position as soon as possible.

### To run the calibration code

First, stop the `robot.service` and start `calibrate_servos.py`.
The pulse width for our servos is as follows:

By following the [datasheet](https://github.com/microrobotics/DS3235-270/blob/master/DS3235-270_datasheet.pdf) of our servo, which says

`max_pulse_width = 2500` $\mu$ seconds

`min_pulse_width = 500` $\mu$ seconds

Thus entire range of pulse width lies $\in$ [2500,500]
So the width of the pulse is $2500-500=2000 \mu$ seconds

And the maximum allowed rotation electrically is $180\degree$

Thus pulse width for rotating $1\degree$ is

$$
\frac{2500-500\mu sec}{180\degree} = 11.111 \mu sec
$$

By default the values provided was $11.333 \mu sec$ which we have to override in `calibrate_servos.py`

Final calibration matrix is as follows. Note these values are not the final values and are subject to change as we continue to improve the design.

| Servo name | Offset Angle | Final angle |
| ---------- | ------------ | ----------- |
| J1         | -34          | 79          |
| J2         | -38          | 83          |
| J3         | 35           | -85         |
| J4         | -40          | 40          |
| J5         | -41          | 86          |
| J6         | 30           | -75         |
| J7         | -44          | 44          |
| J8         | -49          | 94          |
| J9         | 38           | -83         |
| J10        | -48          | 48          |
| J11        | -46          | 91          |
| J12        | 36           | -81         |

## 6. Running the robot

Before starting the robot, we need to make sure that the service `joystick.service` is running. This service is an instance of the python code `Joystick.py` in the folder `Pupper Command`. The code is used to interface the joystick with the robot. To check whether it is already running

```console
pupper@pupper sudo systemctl status joystick.service
```

If the service is not running, run it using the command

```console
pupper@pupper sudo systemctl start joystick.service
```

To run the robot using the controller

```console
pupper@pupper sudo pigpiod
pupper@pupper cd StanfordQuadruped/
pupper@pupper/StanfordQuadruped/ python3 run_robot.py
```

The file `run_robot.py` is the entry point for starting the robot.
By default, there is a service `robot.service` located in the root of the project folder which directs the shell environment to run the python command run_robot.py using python3.

### Jittering and GPIO daemon (pun intended)

The service also directs the shell environment to activate Raspberry Pi's GPIO pins prior to activating the robot by running the command `sudo pigpiod` to activate the Pi's GPIO daemon service. Without this command being issued in the first place `run_robot.py` can not run. Thus when we are manually starting the robot we need to make sure that the GPIO daemon is running and the command is activated exactly once.

If the command `sudo pigpiod` is issued more than once, the shell will prompt an error that a shared resource is being used by multiple processes. This will cause cause a race condition and wrong pwm signals will be delivered to the GPIO pins. **Thus to stop the jittering** we need to restart the Raspberry Pi.

**NOTE:** The service `robot.service` runs the command `sudo pigpiod` once before the service starts. Thus if the service is running, there is nothing else we have to do. Just press `L1 (or LB)` on the controller to activate the robot. The logs of the program will be visible in the service logs by `sudo systemctl status robot.service`.

**But** if we want to run the robot manually, first we need to stop `robot.service`

First check whether the service is already running

```console
pupper@pupper/StanfordQuadruped/ sudo systemctl status robot.service
```

Stop the service if it is already running

```console
pupper@pupper/StanfordQuadruped/ sudo systemctl stop robot.service
```

Then run the code

```console
pupper@pupper/StanfordQuadruped/ python3 run_robot.py
```

## 7. Controlling

After the robot is activated using `L1 (or LB)` one can run the robot.
Make sure the controller is in X-input mode and the mode button on the controller is not lit up.
You can debug the commands from the controller on the screen, `run_robot.py` logs all the commands that are being sent from the controller.
If the light on the mode button is on, that means the analog sticks are emulating the d-pad buttons. Thus only discrete value of `1` and `-1` are obtained by the program.

### Pupper can transition to 3 modes.

1. Standing
2. Squatting
3. Normal

Cycle among each of these modes by pressing the `A (green)` button on the controller. When the robot is in normal mode, press `R1 (or RB)` to activate walking mode. This would allow the controller to control pupper using the analog sticks. Left analog stick can be used to move it forwards or backwards.
Press `R1 (or RB)` once more to reset to normal mode. Here one can set the heights of the joints and legs by pressing `X`, `B` or `Y` buttons on the controller. Pupper can also sit by lowering its lower legs and straightening its front legs.

## 8. Things to do

1. Mount the battery to the bottom of the robot and fasten it with electrical tape and zip-ties.
2. Test the buck converter whether proper 5 volts are coming on the output pins or not.
3. Make an over-voltage protection circuit with zener diode.
4. We have to recalibrate the robot after the aluminum legs arrive.
5. We have to change the PCB design so the signal for J3 comes from GPIO pin `20`.

## 9. Checklist of things which are needed before connecting the PCB to the raspberry pi.

1.  Check all the pins from raspberry's GPIO by hooking them up with an oscilloscope and verifying whether the signals are correct or not. Use a female header to stab the PI's GPIO pin and take the male end of that wire and hook them to the oscilloscope. (Also take a ground pin out from the Pi for hooking the ground lead from the probe) For instance, for our servos, the period of the signal is $20$ _ms_ and lowest admitted duty cycle is $\frac{4}{20}$ _ms_. This should be verified for the entire range of permissible duty cycles for the servo's min and max positions.
    In our case, we did not get a proper signal for GPIO pin `4` for servo J3, thus we changed the pin number to GPIO `20` and added a jumper wire from the same pin to J3's signal header.

2.  Take the multimeter to short circuit testing mode, (a buzzer will make sound when the two leads of the meter are shorted).
    Then probe

        a. Each ground pin with every other pin and check whether those points which should be ground are shorted.

        b. Each power pin with every other pin and check that no pin other than the pins meant to supply power are shorted or not

        c. Each signal pin (where the servos plug in) and the Pi's header pins and test whether the signal pins are properly connected and whether any other pin is shorted with the signal pins.

        d. Most importantly, check whether Vcc and Gnd are not shorted!

This will make sure that all connections are proper and there is no harm to the components after connecting the PCB to the Raspberry Pi and powering it on.

Power the raspberry Pi from the power bank. Later a buck converter and a protection circuit will also be used.
