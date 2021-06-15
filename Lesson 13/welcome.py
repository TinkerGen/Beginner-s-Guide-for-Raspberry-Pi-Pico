from machine import Pin,I2C,PWM
from utime import sleep
from servo import SERVO
from lcd1602 import LCD1602
from buzzer import Music

servo = SERVO(Pin(20))
miniPir = Pin(18, Pin.IN)
pwm = PWM(Pin(27))
mu = Music(pwm)
i2c = I2C(1,scl=Pin(7), sda=Pin(6), freq=400000)
d = LCD1602(i2c, 2, 16)

while True:
    if miniPir.value()== 1:
        print('Motion Detected')
        servo.turn(180)
        d.display() 
        sleep(1)
        d.clear()
        d.print('Welcome') 
        
        mu.music(4)
        sleep(0.25)
        mu.music(0)
        sleep(0.1)  
        mu.music(4)
        sleep(0.25)   
        mu.music(0)
        sleep(0.1)  
        mu.music(4)
        sleep(0.5)  
        mu.music(0)
        sleep(0.1)
    
        mu.music(4)
        sleep(0.25) 
        mu.music(0)
        sleep(0.1)
        mu.music(4)
        sleep(0.25)
        mu.music(0)
        sleep(0.1) 
        mu.music(4)
        sleep(0.5)   
        mu.music(0)
        sleep(0.1)
     
        mu.music(4)
        sleep(0.25)
        mu.music(6)
        sleep(0.25)
        mu.music(2)
        sleep(0.35)
        mu.music(3)
        sleep(0.15) 
        mu.music(4)
        sleep(1)  
        mu.music(0)
        sleep(0.1)
        
        servo.turn(0)
