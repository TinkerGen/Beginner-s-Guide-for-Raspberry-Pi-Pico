from ws2812 import WS2812
from machine import I2C,Pin,ADC
from utime import sleep

led = WS2812(18,1)
LIGHT_SENSOR = ADC(0)
SOUND_SENSOR = ADC(1)

while True:
    average = 0
    light = LIGHT_SENSOR.read_u16()/256
    for i in range (1000):
        noise = SOUND_SENSOR.read_u16()/256
        average += noise
    noise = average/1000
    print(noise)
    
    if light < 80:
        led.pixels_fill((255,255,255))
        led.pixels_show()
        sleep(0.2)
    else:
        if noise < 25:
            led.pixels_fill((0, 255, 0))
            led.pixels_show()
            sleep(1)
        if noise >= 25 and noise < 50:
            led.pixels_fill((255, 255, 0))
            led.pixels_show()
            sleep(1)
        if noise >= 50:
            led.pixels_fill((255, 0, 0))
            led.pixels_show()
            sleep(1)