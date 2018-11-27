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
MODE_REFLECT = 'REFLECT'
mcolor = ColorSensor(INPUT_1)
lcolor = LightSensor(INPUT_2)
rcolor = LightSensor(INPUT_3)
mr = LargeMotor(OUTPUT_A)
ml = LargeMotor(OUTPUT_B)

# print('Auto Driver TubeBotEZ.py')
# # File EV3 Python TubeBot.py
# ev3.Sound.speak('Exterminate').wait()


def test():
    if(lcolor.reflected_light_intensity > 20 and rcolor.reflected_light_intensity < 20):
        turnright()
    elif(lcolor.reflected_light_intensity > 20 and lcolor.reflected_light_intensity < 20):
        turnleft()
    if(lcolor.reflected_light_intensity < 20 and mcolor.color == 0 and rcolor.reflected_light_intensity < 20):
        line_black = True
        drive()
def drive():
    while(line_black):
        tank_drive = MoveTank(OUTPUT_A, OUTPUT_B)
        tank_drive.on_for_rotations(SpeedPercent(80), SpeedPercent(80), 1)
        if(lcolor.reflected_light_intensity > 20 or mcolor.color != 1 or rcolor.reflected_light_intensity > 20):
            line_black == False
    if(line_black == False):
        test()
if(mcolor.color == 0 and lcolor.reflected_light_intensity < 20 and rcolor.reflected_light_intensity < 20):
    line_black = True
    drive()
else:
    line_black = False
    test()
def turnleft():
    while(line_black == False):
        tank_drive.on_for_rotations(SpeedPercent(80), SpeedPercent(0), 3)
        test()
def turnright():
    while(line_black == False):
        tank_drive.on_for_rotations(SpeedPercent(0), SpeedPercent(80), 3)
        test()
