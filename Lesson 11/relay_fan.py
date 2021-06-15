from machine import Pin
from time import sleep
button = Pin(16,Pin.IN)
fan = Pin(18,Pin.OUT)
relay = Pin(20,Pin.OUT)

while True:
    fan.value(1)
    while button.value() == 1:
        relay.toggle()
        sleep(1)  