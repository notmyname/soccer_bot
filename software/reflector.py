from machine import Pin

init_done = False


def init():
    global source, sensor, init_done
    source = Pin(22)
    sensor = Pin(4)
    sensor.init(sensor.IN)
    source.init(source.OUT)
    source.value(100)  # why this magic number?
    init_done = True


def is_blocked():
    # 0 is blocked
    # 1 is unubstructed
    if init_done:
        return sensor.value() == 0
    return None  # could raise here instead
