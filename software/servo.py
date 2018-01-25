from machine import PWM
from machine import Pin

import time


def kick():
    motor = PWM(Pin(16))
    motor.freq(50)
    motor.duty(25)

    time.sleep(1)

    motor.duty(0)
