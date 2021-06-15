from machine import Pin
from utime import sleep
from servo import SERVO
servo = SERVO(Pin(20))
miniPir = Pin(18, Pin.IN)

while True:
    if miniPir.value()== 1:
        print('Motion Detected')
        servo.turn(180)
        sleep(10)
        
        servo.turn(0)