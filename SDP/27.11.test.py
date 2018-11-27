#!/usr/bin/env python3
#import time
# from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_B, SpeedPercent, MoveTank

# def main():
#     time.sleep(5)
#     tank_drive = MoveTank(OUTPUT_A, OUTPUT_B)
#     tank_drive.on_for_seconds(SpeedPercent(100), SpeedPercent(100), 3)

# if __name__ == '__main__':
#     main()
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
def test():
    if(lcolor.reflected_light_intensity > 33 and rcolor.reflected_light_intensity < 33):
        turnright()
    if(lcolor.reflected_light_intensity < 33 and lcolor.reflected_light_intensity > 33):
        turnleft()
if(mcolor.color == 1 and lcolor.reflected_light_intensity < 33 and rcolor.reflected_light_intensity < 33):
    line_black = True
    drive()
else:
    test()
def drive():
    while(line_black):
        tank_drive = MoveTank(OUTPUT_A, OUTPUT_B)
        tank_drive.on_for_rotations(SpeedPercent(80), SpeedPercent(80), 10)
        if(lcolor.reflected_light_intensity > 33 or mcolor.color != 1 or rcolor.reflected_light_intensity > 33):
            line_black == False
    if(line_black == False):
        test()
def turnleft():
    while(line_black == False):
        mr.on_for_rotations(SpeedPercent(100),20)
        ml.on_for_rotations(SpeedPercent(10),20)
        if(lcolor.reflected_light_intensity < 33 and mcolor.color == 1 and rcolor.reflected_light_intensity < 33):
            line_black = True
            drive()
def turnright():
    while(line_black == False):
        mr.on_for_rotations(SpeedPercent(10),20)
        ml.on_for_rotations(SpeedPercent(100),20)
        if(lcolor.reflected_light_intensity < 33 and mcolor.color == 1 and rcolor.reflected_light_intensity < 33):
            line_black = True
            drive()
