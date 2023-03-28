# Documentation for Pupper

1. [Parts sourcing](#1-parts-sourcing)
2. [Assembly](#2-assembly)
3. [Connections](#3-connections)
4. [Code](#4-code)

## 1. Parts sourcing.

Please refer to [This spreadsheet](https://docs.google.com/spreadsheets/d/1AzzCM8UDrbhDfgtIsiQplI5SMlo7OLG8/edit#gid=1202520655). Part sourcing is listed here comprehensively.

For building the qudruped's body and legs, we have used 5mm fibre sheets. Ideally it should be carbon fibre. But we could not find a vendor who could cut the carbon fibre sheets according to our specifications. Also laser cutting of carbon fibre is not possible in the lab. The next best choice was to use acrylic fibre and that is what we used. $3$ mm thickness for legs and $5$ mm thickness for the base and top.

All the strucural elements are taken from [here](https://a360.co/2TEh4gQ)
[![Pupper](/img/Pupper.png "Codey the Codecademy mascot")](https://stanford195.autodesk360.com/g/shares/SH919a0QTf3c32634dcfedf61e031f673710)

### Laser Cut parts

| Part name                 | Quantity | Thickness (mm) |
| ------------------------- | -------- | -------------- |
| Acrylic fibre plate top   | 1        | 5              |
| Acrylic fibre plate bottm | 1        | 5              |
| Lower leg                 | 4        | 3              |
| Upper leg                 | 4        | 3              |

To obtain the design of the above parts, we extracted each of the above mentioned prefab from the fusion 360 model. For laser cutting, we had to project the legs, and the base on a 2d surface in fusion, and extract the traces. Then we used laser cad for some final retouching.

_Note:_ The design provided here has two holes in the upper legs, both of them are useless as they do not fit our servo horn. So we had to modify the position of the hole in laser CAD to be $0.85$ mm from the begenning of the curvature.

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
The [Gerber files](https://github.com/stanfordroboticsclub/Pupper-Raspi-PDB/) could be used to print the PCB using any standard PCB manufacturer. _NOTE_ 2 oz copper should be used for the traces.

## 2. Assembly

Pupper has 4 legs, each with 3 sets of [servos](https://robokits.co.in/motors/rc-servo-motor/ultra-torque-metal-gear-35kgcm-coreless-stainless-steel-pinion-standard-servo-motor). These servos are placed inside 3D printed hip joints.

### All reference images are placed under folder [3D printed files](/img)

![Servo placement and numbering](/img/body7com.jpg)

### Hip assembly

All the servos should be housed inside hip joints in the following way:

1. First, screw metallic disc with $J1,J4,J7,J10$. _Important_: apply some hot glue after fixing the disc tightly with the servo.

2. Take inner hip and screw 4 black m4x6 screws that came with the servos to the disc.

3. Place $J2,J5,J8,J11$ in the inner hip and use m3x20 screws to tighten the side of the hip facing away from the disc.

4. _Note:_ Tightening should be enough such that the screw pokes out from the other side of the inner hip. Here we need to fasten the 20mm spacers. Tighten the servo with m3x10 screws (for the remaining two holes)

_Choice of the screw is important. The horn should be facing away from the 4 spacers and should be able to rotate freely without any obstruction. So the screws should be tightened upto that extent only which does not cause any obstruction in the horn's way_

5. Place the other set of 20mm spacers on the screws fasteneded onthe sid eof the plastic case, i.e they do not tighten the servo.
   Then the plastic disc that came with the servos should be attached ring side facing up, to $J5,J2,J8,J11$ along with 25T servo horn beneath the disc (which came with the servos as well).

_The disc is used to create spacing for the legs. It makes sure that the legs don't slip while rotating._

6. Attach 25T horn to $J3,J6,J9,J12$. This horn should parallel to the other set of horns i.e $J5,J2,J8,J11$ and should face the free side of the enclosure.

### Leg assembly

Take the laser cut parts, upper legs and lower legs and place a thrust bearing between the two joints, and another bearing to the side of the screw head. The flat end of the lower leg should touch the ground and the lower leg should be facing outwards, away from the body. Place a m3x16 screw between the sandwitched joints and tighten a nilon locknut from the other end. This way prepare all the 4 legs.

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

All the servos should be connected to the [PCB](https://github.com/stanfordroboticsclub/Pupper-Raspi-PDB/), whcich is connected to the Raspberry Pi. The PCB is well marked and the signal side of the connector should face the GPIO headers.

![Connection](/img/body7pre.jpg)
The pigtail connector (Big wire on the right) is connected to the battery powering 7.4 volts and that power is converted to 5 volts using a voltage converter on the left. The output of the voltage converter _should_ be 5 Volts which directly plugs in our PCB where it is marked +5 volts and ground.

## What went wrong

Never try to power the RPi with anything less than 4.75 volts and 5.25 volts. This was the mistake which costed us our Raspberry Pi 3 model B plus.
I tested the output of the voltage converter, which showed 5 volts and I powered on the Raspberry Pi. It turned on and I SSHed into the Pi. Tested one servo and it was all good. Then I turned off the RPi using shutdown command from SSH.

However next time before turning on the RPi I did not check the voltage and it didn't turn on. I quickly unplugged the battery and then disconnected the board. Later when I was testing the voltage converter seperately, the output of the voltage converter was same as the input with some voltage drop i.e it was showing 6.8 volts!

Assuming our worst fear, I waited for another day and checked online forums whether the RPi has polyfuse or not. It turns out that the Raspberry Pi has polyfuse, but they are placed between the input and the SOC so the GPIO side where we plugged in our power supply had no protection.

I double checked all the [testing points](https://ozzmaker.com/testing-points-raspberry-pi/) in the Pi and confirmed that the raspberry pi has indeed been shorted.

**NOTE** Always check the power supply before plugging into the Pi. Since it is powered by micro USB we might be tempted to power it on from our computer's USB port but **DON'T** do that as that port can never provide enough current to the board. Similarly always check for faulty power supply and voltage levels before powering on the Pi.

## 4. Code

Code for the quadruped has been taken from the open source project by stanford robotics group [here](https://github.com/stanfordroboticsclub/StanfordQuadruped) and the joystick controller code has been taken from [here](https://github.com/stanfordroboticsclub/PS4Joystick). The code is very well documented and self explainatory but it had an [issue](#added-wireddongle-controller-support)

I did not use the image they provided for flashing the SD card. The image is way to old and I faced many problems while updating repositories. Thus I ended up using a standard 32 bit distribution of [Raspbian](https://www.raspberrypi.com/software/operating-systems/#raspberry-pi-os-32-bit).

After etching the sd card with [Raspberry Pi's image software](https://www.raspberrypi.com/software/) I booted into the Pi.

Raspbian provides a GUI so our job was easier. Later the plan was to remove the Desktop Environment and only keep the CLI to reduce system overhead.
With the pi connected to USB mouse, keyboard and a display, we set up wifi on the pi so we could use it in headless mode in the future. All successive accesses were made using VNC or SSH. And the pi was only connected to power using a wall adapter which supported 3A 5V.

### Added wired/dongle controller support

The default code They provided had only support for a PS4 dualshock controller. And not only that, the internal code for the working of the robot, is also very much intertwined with the proprietary code it shipped with. Thus I had to rewrite the code to add support for wired / standard bluetooth controller with a dongle like the logitech f710 controller we used. ![controller](/img/controller.jpg)

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
