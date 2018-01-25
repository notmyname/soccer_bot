"""
import disco
disco.write_led3(disco.red)
disco.write_led2(disco.red)
disco.write_led2(disco.green)
disco.write_led1(disco.blue)
"""

from machine import Pin
from neopixel import NeoPixel

from random import randint
import time

led3 = NeoPixel(Pin(2), 3, timing=True)
led2 = NeoPixel(Pin(2), 2, timing=True)
led1 = NeoPixel(Pin(2), 1, timing=True)

cur1 = [0, 0, 0]
cur2 = [0, 0, 0]
cur3 = [0, 0, 0]

green = [64, 0, 0]
red = [0, 64, 0]
blue = [0, 0, 64]
off = [0, 0, 0]
white = on = [127, 127, 127]

def write_led1(color_array):
    global cur1, cur2, cur3
    cur1 = color_array

    led1.fill(cur1)
    led1.write()

def write_led2(color_array):
    global cur1, cur2, cur3
    cur2 = color_array

    led2.fill(cur2)
    led1.fill(cur1)
    led2.write()
    led1.write()

def write_led3(color_array):
    global cur1, cur2, cur3
    cur3 = color_array

    led3.fill(cur3)
    led2.fill(cur2)
    led1.fill(cur1)
    led3.write()
    led2.write()
    led1.write()

def disco():
    for i in range(1000):
        p1 = [randint(0, 255), randint(0, 255), randint(0, 255)]
        p2 = [randint(0, 255), randint(0, 255), randint(0, 255)]
        p3 = [randint(0, 255), randint(0, 255), randint(0, 255)]

        led1.fill(p1)
        led2.fill(p2)
        led3.fill(p3)

        led3.write()
        led2.write()
        led1.write()

        time.sleep(.1)

