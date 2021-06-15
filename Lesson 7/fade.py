import utime
from machine import Pin,PWM

LED_PWM=PWM(Pin(18))

val=0
LED_PWM.freq(500)
while True:
    while val<65535:
        val=val+50
        utime.sleep_ms(1)   
        LED_PWM.duty_u16(val)
    while val>0:
        val=val-50
        utime.sleep_ms(1)
        LED_PWM.duty_u16(val)