from machine import ADC
from utime import sleep

ROTARY_ANGLE_SENSOR = ADC(0)  

while True:
    print(ROTARY_ANGLE_SENSOR.read_u16())
    sleep(1)    