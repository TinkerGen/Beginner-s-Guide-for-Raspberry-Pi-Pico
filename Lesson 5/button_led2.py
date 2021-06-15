import machine
import utime

BUTTON = machine.Pin(16,machine.Pin.IN)
LED = machine.Pin(18,machine.Pin.OUT)

val = 0

while True:
    if BUTTON.value() == 1:
        val = val+1
        utime.sleep(1)
    elif val == 2:
        val = 0
        utime.sleep(1)
    LED.value(val)