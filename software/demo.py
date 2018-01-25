import reflector
import servo
import time
from lib import lolibot

from machine import PWM
from machine import Pin

import configuration.lolibot


def kick_hard():
    motor = PWM(Pin(16))
    lolibot.motor_action(lolibot.motor_commands["reverse"])
    time.sleep(.25)
    motor.freq(50)
    motor.duty(25)
    lolibot.motor_action(lolibot.motor_commands["forward"])
    time.sleep(.5)
    motor.duty(0)
    lolibot.motor_action(lolibot.motor_commands["stop"])


lolibot.initialise(configuration.lolibot.settings)
reflector.init()

def start():
    while True:
        if reflector.is_blocked():
            kick_hard()
        time.sleep(.5)
