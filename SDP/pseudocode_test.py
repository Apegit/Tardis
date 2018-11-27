#!/usr/bin/env python3

import time
from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_B, SpeedPercent, MoveTank
from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_3
from ev3dev2.sensor.lego import TouchSensor
from ev3dev2.led import Leds
from ev3dev2.sensor.lego import ColorSensor, LightSensor

Kp = 520
Ki = 20
Kd = 10
offset = 17
Tp = 40
integral = 0
lastError = 0
dervitave = 0
lcolor = LightSensor(INPUT_2)
mr = LargeMotor(OUTPUT_A)
ml = LargeMotor(OUTPUT_B)
while(True):
    lightvalue = lcolor.reflected_light_intensity
    error = lightvalue - offset
    integral = integral + error
    dervitave = error - lastError
    turn = Kp * error + Ki * integral + Kd * dervitave
    turn = turn / 100
    powerA = Tp + turn
    powerC = Tp - turn
    ml.on(SpeedPercent(powerA))
    mr.on(SpeedPercent(powerC))
    lastError = error
    