from lcd1602 import LCD1602
from dht11 import *
from machine import I2C,Pin,ADC
from utime import sleep

i2c = I2C(1,scl=Pin(7), sda=Pin(6), freq=400000)
d = LCD1602(i2c, 2, 16)
d.display()
dht2 = DHT(16)
miniFan = machine.Pin(18,machine.Pin.OUT)

while True:
    temp = dht2.readTemperature()#temp:   
    sleep(1)
    d.clear()
    d.setCursor(0,0)
    d.print("Temp:"+str(temp))
    sleep(1)
    if temp > 26:
        miniFan.value(1)
    else:
        miniFan.value(0)