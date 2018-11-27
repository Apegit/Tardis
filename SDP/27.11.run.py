#!/usr/bin/env python3
# so this script/program can be run from Brickman

from ev3dev2.ev3 import *
from time import sleep

import ev3dev2.ev3 as ev3

print('Auto Driver TubeBotEZ.py')
# File EV3 Python TubeBot.py
ev3.Sound.speak('python Tube Robot easy 2').wait()

LeftWheel = LargeMotor('outA')
RightWheel = LargeMotor('outB')
ir = InfraredSensor()
# assert ir.connected, "Connect a single infrared sensor to any sensor port"

ts = TouchSensor()
# assert ts.connected, "Connect a touch sensor to any port"
# can have 2 statements on same line if use semi colon

# Put the infrared sensor into proximity mode.
ir.mode = 'IR-PROX'

DelayTime = 0
Target = 10
Error = 0
Integral = 0
Derivative = 0
LastError = 0
Kp = 3
Ki = 0
Kd = 0
PID = 1
Time = 400
LeftPower = 1
RightPower = 1
MaxTurnPower = 200
Iteration = 0
Distance = 0
SpeedFactor = 300
y = 0
Speed = 100
OldDistance = 1000
DistanceL = 1
DistanceR = 2

Beginning = '{:3d}        Start                        Left Distance {:>4.0f}     Right Distance {:>4.0f}'.format(Iteration, DistanceL, DistanceR)
Ending = '        LeftPower {:>5.0f}    RightPower {:>5.0f}'.format(
    LeftPower, RightPower)
print(Beginning, Ending)

#ev3.Sound.speak('Start').wait()
sleep(DelayTime)
Battery = True
#Sound.speak('Point 1')
while Battery:
    Leds.all_off()
#    Leds.set_color(Leds.UP, Leds.GREEN)
#    Leds.set_color(Leds.DOWN, Leds.GREEN)
    Leds.set_color(Leds.LEFT, Leds.GREEN)
    Leds.set_color(Leds.RIGHT, Leds.GREEN)
    # Phase 1
    if True:

#        Sound.speak('SQUARE WALL')
        sleep(DelayTime)
        DistanceL = ir.value()
        LeftWheel.run_to_rel_pos(position_sp=20, speed_sp=900, stop_action="hold")
        RightWheel.run_to_rel_pos(position_sp=-20, speed_sp=900, stop_action="hold")
        #sleep(DelayTime)   # Give the motor time to move
        #LeftWheel.stop()
        LeftWheel.wait_while('running')
        RightWheel.wait_while('running')
        #sleep(1)
        DistanceR = ir.value()
        if DistanceL != DistanceR:
            if DistanceL < DistanceR:
                while DistanceL < DistanceR:
#                    print('in Left loop')

#                    Sound.speak('Left').wait()
                    sleep(DelayTime)   # Give the motor time to move
                    DistanceR = ir.value()
                    LeftWheel.run_to_rel_pos(position_sp=-20, speed_sp=900, stop_action="hold")
                    RightWheel.run_to_rel_pos(position_sp=20, speed_sp=900, stop_action="hold")
                    sleep(DelayTime)   # Give the motor time to move
                    LeftWheel.stop()
                    LeftWheel.wait_while('running')
                    sleep(DelayTime)
                    DistanceL = ir.value()
                    Iteration += 1
                    Beginning = '{:3d}      Left      in                    Left Distance {:>4.0f}     Right Distance {:>4.0f}'.format(Iteration, DistanceL, DistanceR)
                    Ending = '        LeftPower {:>5.0f}    RightPower {:>5.0f}'.format(
                        LeftPower, RightPower)
                    print(Beginning, Ending)
#                ev3.Sound.speak('Re set Right').wait()
                LeftWheel.run_to_rel_pos(position_sp=20, speed_sp=900, stop_action="hold")
                RightWheel.run_to_rel_pos(position_sp=-20, speed_sp=900, stop_action="hold")
                sleep(DelayTime)   # Give the motor time to move
                LeftWheel.stop()
                LeftWheel.wait_while('running')
                sleep(DelayTime)
                Iteration += 1
                Beginning = '{:3d}       Left out                     Left Distance {:>4.0f}     Right Distance {:>4.0f}'.format(Iteration, DistanceL, DistanceR)
                Ending = '        LeftPower {:>5.0f}    RightPower {:>5.0f}'.format(
                    LeftPower, RightPower)
                print(Beginning, Ending)
                Sound.beep()
            else:
                while DistanceR < DistanceL:
#                    print('in while close loop')

#                    ev3.Sound.speak('Right').wait()
                    sleep(DelayTime)
                    DistanceL = ir.value()
                    LeftWheel.run_to_rel_pos(position_sp=20, speed_sp=900, stop_action="hold")
                    RightWheel.run_to_rel_pos(position_sp=-20, speed_sp=900, stop_action="hold")
                    sleep(DelayTime)  # Give the motor time to move
                    LeftWheel.stop()
                    LeftWheel.wait_while('running')
                    sleep(DelayTime)
                    DistanceR = ir.value()
                    Iteration += 1
                    Beginning = '{:3d}          Right   in                   Left Distance {:>4.0f}     Right Distance {:>4.0f}'.format(Iteration, DistanceL, DistanceR)
                    Ending = '        LeftPower {:>5.0f}    RightPower {:>5.0f}'.format(
                        LeftPower, RightPower)
                    print(Beginning, Ending)

#                ev3.Sound.speak('Reset Left').wait()
                LeftWheel.run_to_rel_pos(position_sp=-30, speed_sp=900, stop_action="hold")
                RightWheel.run_to_rel_pos(position_sp=30, speed_sp=900, stop_action="hold")
                sleep(DelayTime)  # Give the motor time to move
                LeftWheel.stop()
                LeftWheel.wait_while('running')
                sleep(DelayTime)
                Iteration += 1
                Beginning = '{:3d}          Right   in       out            Left Distance {:>4.0f}     Right Distance {:>4.0f}'.format(Iteration, DistanceL, DistanceR)
                Ending = '        LeftPower {:>5.0f}    RightPower {:>5.0f}'.format(
                    LeftPower, RightPower)
                print(Beginning, Ending)

                Sound.beep()

        Beginning = '{:3d}       Finished                     Left Distance {:>4.0f}     Right Distance {:>4.0f}'.format(Iteration, DistanceL, DistanceR)
        Ending = '        LeftPower {:>5.0f}    RightPower {:>5.0f}'.format(
            LeftPower, RightPower)
        print(Beginning, Ending)
        Sound.beep()

        Beginning = '{:3d}    Target {:3.0f}    Distance {:>4.0f}'.format(Iteration, Target, Distance)
        Ending = '    Delta {:>4.0f}    Integral {:>5.0f}    Derivative {:>5.0f}    LastError {:>5.0f}    PID {:>5.0f}    SpeedFactor {:>5.0f}    LeftPower {:>5.0f}    RightPower {:>5.0f}'.format(
            Error, Integral, Derivative, LastError, PID, SpeedFactor, LeftPower, RightPower)
        print(Beginning, Ending)
        sleep(DelayTime)

        while not ts.value():  # Stop program by pressing touch sensor button
                # Infrared sensor in proximity mode will measure distance to the closest
                # object in front of it.

#                    Sound.speak('FORWARD')
                    sleep(DelayTime)
                    Iteration += 1
                    Distance = ir.value()
                    if Distance < Target:
#                        print('in Distance < Target loop')
                        Leds.set_color(Leds.LEFT, Leds.RED)
                        Leds.set_color(Leds.RIGHT, Leds.GREEN)

#                        Sound.speak('RIGHT')
                        sleep(DelayTime)
                    else:
#                        print('Close else')
                        Leds.set_color(Leds.LEFT, Leds.GREEN)
                        Leds.set_color(Leds.RIGHT, Leds.RED)

#                        Sound.speak('LEFT')
                        sleep(DelayTime)

                    Error = Target - Distance
                    Integral += Error
                    Derivative = Error - LastError

                    if Integral < -MaxTurnPower:
                        Integral = -MaxTurnPower
                    if Integral > MaxTurnPower:
                        Integral = MaxTurnPower

                    if Derivative < -MaxTurnPower:
                        Derivative = -MaxTurnPower
                    if Derivative > MaxTurnPower:
                        Derivatine = MaxTurnPower

                    PID = Kp * Error + Ki * Integral + Kd * Derivative

                    if PID < -MaxTurnPower:
                        PID = -MaxTurnPower
                    if PID > MaxTurnPower:
                        PID = MaxTurnPower

                    LeftPower = SpeedFactor + PID
                    RightPower = SpeedFactor - PID

                    if LeftPower < -900:
                        LeftPower = -901
                    if LeftPower > 900:
                        LeftPower = 902

                    if RightPower < -900:
                        RightPower = -903
                    if RightPower > 900:
                        RightPower = 904

                    Beginning = '{:3d}    Target {:3.0f}    Distance {:>4.0f}'.format(Iteration, Target, Distance)
                    Ending = '    Delta {:>4.0f}    Integral {:>5.0f}    Derivative {:>5.0f}    LastError {:>5.0f}    PID {:>5.0f}    SpeedFactor {:>5.0f}    LeftPower {:>5.0f}    RightPower {:>5.0f}'.format(
                        Error, Integral, Derivative, LastError, PID, SpeedFactor, LeftPower, RightPower)

                    print(Beginning, Ending)
                    LeftWheel.run_timed(time_sp=Time, speed_sp=LeftPower)
                    RightWheel.run_timed(time_sp=Time, speed_sp=RightPower)

                    LastError = Error

#    Leds.set_color(Leds.UP, Leds.RED)
#    Leds.set_color(Leds.DOWN, Leds.RED)
    Leds.set_color(Leds.LEFT, Leds.RED)
    Leds.set_color(Leds.RIGHT, Leds.RED)
    LeftWheel.run_to_rel_pos(position_sp=-20, speed_sp=900, stop_action="hold")
    RightWheel.run_to_rel_pos(position_sp=-400, speed_sp=900, stop_action="hold")
    Sound.beep()
