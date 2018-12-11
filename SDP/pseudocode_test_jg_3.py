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
#ccolor = ColorSensor(INPUT_1)
mr = LargeMotor(OUTPUT_A)
ml = LargeMotor(OUTPUT_B)
a = .175
def kalibrierung(a, l1, l2):
    return (l2 - l1) * a

d = kalibrierung(a, lcolor1.reflected_light_intensity, lcolor2.reflected_light_intensity) 

def firstwhile():
    global switch1, switch2 
    lcolor1 = LightSensor(INPUT_2)
    lcolor2 = LightSensor(INPUT_3)
    Kp = 140
    Ki = 0
    Kd = 0
    offset = d
    Tp = 50
    integral = 0
    lastError = 0
    dervitave = 0
    while(True):
        while((lcolor2.reflected_light_intensity - lcolor1.reflected_light_intensity) < d ):
            error = lcolor1.reflected_light_intensity - offset
            integral = integral + error
            dervitave = error - lastError
            turn = Kp * error + Ki * integral + Kd * dervitave
            turn = turn / 100
            powerA = Tp - turn
            powerC = Tp + turn
            ml.on(SpeedPercent(powerA))
            mr.on(SpeedPercent(powerC))
            lastError = error

        while((lcolor2.reflected_light_intensity - lcolor1.reflected_light_intensity) > d ):
            error = lcolor2.reflected_light_intensity - offset
            integral = integral + error
            dervitave = error - lastError
            turn = Kp * error + Ki * integral + Kd * dervitave
            turn = turn / 100
            powerA = Tp + turn
            powerC = Tp - turn
            ml.on(SpeedPercent(powerA))
            mr.on(SpeedPercent(powerC))
            lastError = error

        powerA = Tp + turn
        powerC = Tp + turn
        ml.on(SpeedPercent(powerA))
        mr.on(SpeedPercent(powerC))
        lastError = error

       


#def secwhile():
    global switch1, switch2
    lcolor1 = LightSensor(INPUT_2)
    lcolor2 = LightSensor(INPUT_3)
    Kp = 110
    Ki = 0
    Kd = 0
    offset = d
    Tp = 30
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
        powerA = Tp + turn
        powerC = Tp - turn
        last_step = 'LTR'
        ml.on(SpeedPercent(powerA))
        mr.on(SpeedPercent(powerC))
        lastError = error


# def thirdwhile():
#     #white = 620
#     #black = 637
#     #CALIBRATE()
#     #midpoint = (white - black) / 2 + black
#     midpoint = 20
#     print(ccolor.reflected_light_intensity)
#     kp = 3
#     ki = 0.0
#     kd = 0.0
#     tp = 40
#     lasterror = 0.0
#     stay = True
#     integral = 0.0
#     while(stay):
#         v1, v2, v3 = ccolor.raw
#         print(v1, v2, v3)
#         error = midpoint - v3
#         integral = error + integral
#         derivative = error - lasterror
#         correction = kp * error + ki * integral + kd * derivative
#         lasterror = error
#         while(v3 < 10):
#             powerA = tp 
#             powerB = tp 
#             ml.on(SpeedPercent(powerA))
#             mr.on(SpeedPercent(powerB))

firstwhile()

    



    