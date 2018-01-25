from machine import Pin
from machine import ADC

bat = ADC(Pin(32))

def get_battery_value():
    # this returns a 12-bit number (0-4095)
    # I'm not sure yet what the values map to
    # (4.2v (li battery), 5v (usb poser), 3.3v (chip power))
    return bat.read()
