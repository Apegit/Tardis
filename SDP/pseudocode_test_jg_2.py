#!/usr/bin/env python3

import time
from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_B, SpeedPercent, MoveTank
from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_3
from ev3dev2.sensor.lego import TouchSensor
from ev3dev2.led import Leds
from ev3dev2.sensor.lego import ColorSensor, LightSensor

'''Kp = 520
Ki = 0
Kd = 0
offset = 20
Tp = 30
integral = 0
lastError = 0
dervitave = 0'''
lcolor1 = LightSensor(INPUT_2)
lcolor2 = LightSensor(INPUT_3)
mr = LargeMotor(OUTPUT_A)
ml = LargeMotor(OUTPUT_B)
switch1 = True
switch2 = True
a = 3
def kalibrierung(a, l1, l2):
    return (l2 - l1) * a

d = kalibrierung(a, lcolor1.reflected_light_intensity, lcolor2.reflected_light_intensity)

def firstwhile():
    global switch1, switch2
    lcolor1 = LightSensor(INPUT_2)
    lcolor2 = LightSensor(INPUT_3)
    Kp = 85
    Ki = 0
    Kd = 0
    offset = d
    Tp = 30
    integral = 0
    lastError = 0
    dervitave = 0
    while(switch1):
        if((lcolor2.reflected_light_intensity - lcolor1.reflected_light_intensity) > d):
            switch1 = False
            switch2 = True
        lightvalue1 = lcolor1.reflected_light_intensity
        error = lightvalue1 - offset
        integral = integral + error
        dervitave = error - lastError
        turn = Kp * error + Ki * integral + Kd * dervitave
        turn = turn / 100
        powerA = Tp + turn
        powerC = Tp - turn
        ml.on(SpeedPercent(powerA))
        mr.on(SpeedPercent(powerC))
        lastError = error


def secwhile():
    global switch1, switch2
    lcolor1 = LightSensor(INPUT_2)
    lcolor2 = LightSensor(INPUT_3)
    Kp = 85
    Ki = 0
    Kd = 0
    offset = d
    Tp = 50
    integral = 0
    lastError = 0
    dervitave = 0
    while(switch2):
        if((lcolor1.reflected_light_intensity - lcolor2.reflected_light_intensity) > d):
            switch1 = True
            switch2 = False
        lightvalue2 = lcolor2.reflected_light_intensity
        error = lightvalue2 - offset
        integral = integral + error
        dervitave = error - lastError
        turn = Kp * error + Ki * integral + Kd * dervitave
        turn = turn / 100
        powerA = Tp - turn
        powerC = Tp + turn
        ml.on(SpeedPercent(powerA))
        mr.on(SpeedPercent(powerC))
        lastError = error


while(True):
    firstwhile()
    secwhile()



    