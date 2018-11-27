#!/usr/bin/env python3
import time
from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_B, SpeedPercent, MoveTank
from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_3
from ev3dev2.sensor.lego import TouchSensor
from ev3dev2.led import Leds
from ev3dev2.sensor.lego import ColorSensor, LightSensor
line_black = False
mcolor = ColorSensor(INPUT_1)
lcolor = LightSensor(INPUT_2)
rcolor = LightSensor(INPUT_3)
mr = LargeMotor(OUTPUT_A)
ml = LargeMotor(OUTPUT_B)
if(mcolor.color == 1 and sensorValue(lcolor) < 45 and rcolor.color == 1):
    line_black = True
    drive()
if(line_black == False):
    test()
def drive():
    while(line_black):
        tank_drive = MoveTank(OUTPUT_A, OUTPUT_B)
        tank_drive.on_for_rotations(SpeedPercent(80), SpeedPercent(80), 10)
        if(lcolor.color != 1 or mcolor.color != 1 or rcolor.color != 1):
            line_black == False
    if(line_black == False):
        test()
def test():
    if(lcolor != 1 and rcolor == 1):
        turnright()
    if(lcolor == 1 and rcolor != 1):
        turnleft()
def turnleft():
    while(line_black == False):
        mr.on_for_rotations(SpeedPercent(100),20)
        ml.on_for_rotations(SpeedPercent(10),20)
        if(lcolor.color == 1 and mcolor.color == 1 and rcolor.color == 1):
            line_black = True
            drive()
def turnright():
    while(line_black == False):
        mr.on_for_rotations(SpeedPercent(10),20)
        ml.on_for_rotations(SpeedPercent(100),20)
        if(lcolor.color == 1 and mcolor.color == 1 and rcolor.color == 1):
            line_black = True
            drive()