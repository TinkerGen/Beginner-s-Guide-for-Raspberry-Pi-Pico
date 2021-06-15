from lcd1602 import LCD1602
from machine import I2C,Pin,ADC,PWM
from utime import sleep

ROTARY_ANGLE_SENSOR = ADC(0)
LED_PWM = PWM(Pin(18))
i2c = I2C(1,scl=Pin(7),sda=Pin(6),freq=400000)
LED_PWM.freq(500)
d = LCD1602(i2c,2,16)
d.display()

while True:
    val=ROTARY_ANGLE_SENSOR.read_u16()
    LED_PWM.duty_u16(val)
    sleep(1)
    d.clear()
    d.setCursor(0,0)
    d.print(str(val))
    sleep(1)