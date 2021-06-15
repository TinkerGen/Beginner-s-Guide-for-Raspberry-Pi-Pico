from machine import ADC,Pin
from time import sleep

LED = Pin(16,Pin.OUT)
ROTARY_ANGLE_SENSOR = ADC(1)  
while True:
    print(ROTARY_ANGLE_SENSOR.read_u16())
    if ROTARY_ANGLE_SENSOR.read_u16() > 20000 and ROTARY_ANGLE_SENSOR.read_u16() < 40000:
        LED.value(1)
        sleep(1)
    else:
        LED.value(0)
        sleep(1)