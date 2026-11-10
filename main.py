#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase

# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.

#Variables
sensorTestMode = False

driveSpeed = 250 #200
turnSpeedDif = 23 #15

heightDriveSpeed = 200 #200
ultrasonicDistance = 60 #80

# Initialize EV3 Brick
ev3 = EV3Brick()

# Initialize motors
leftDrive = Motor(Port.A)
rightDrive = Motor(Port.B)
heightDrive = Motor(Port.C)

leftDrive.positive_direction = Direction.COUNTERCLOCKWISE
rightDrive.positive_direction = Direction.CLOCKWISE

# Initialize sensors
colorSensor = ColorSensor(Port.S1)

ultrasonicSensor = UltrasonicSensor(Port.S4)


# Write your program here.
ev3.speaker.beep()

print(turnSpeedDif)

'''
def Drive(speed, turnSpeed):
    if (colorSensor.color() == Color.BLACK):
        leftDrive.run(speed + turnSpeed)
        rightDrive.run(-speed - turnSpeed)
    elif (colorSensor.color() == Color.WHITE):
        leftDrive.run(-speed - turnSpeed)
        rightDrive.run(speed + turnSpeed)
    else:
        leftDrive.run(speed)
        rightDrive.run(speed)

    print(colorSensor.color())
'''

def Drive(speed, turnSpeed):
    if (colorSensor.reflection() <= 50):
        leftDrive.run(speed + turnSpeed)
        rightDrive.run(speed - turnSpeed)
    elif (colorSensor.reflection() > 50):
        leftDrive.run(speed - turnSpeed)
        rightDrive.run(speed + turnSpeed)
    else:
        leftDrive.run(speed)
        rightDrive.run(speed)

def Arm():
    # Check the distance to the control route
    distance = ultrasonicSensor.distance()
    print("Distance to control route: " + str(distance) + " mm")
    
    if (distance < ultrasonicDistance):
        heightDrive.run(-heightDriveSpeed)
        print("Adjusting height upwards")
    if (distance > ultrasonicDistance):
        heightDrive.run(heightDriveSpeed)
        print("Adjusting height downwards")
    else:
        print("Height is correct")
    


while (not Button.CENTER in ev3.buttons.pressed()):
    # Run the motor
    if (not sensorTestMode):
        Drive(driveSpeed, turnSpeedDif)
    print(colorSensor.reflection())

    Arm()
