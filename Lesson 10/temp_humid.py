from lcd1602 import LCD1602
from dht11 import *
from machine import I2C,Pin,ADC
from utime import sleep

i2c = I2C(1,scl=Pin(7), sda=Pin(6), freq=400000)
d = LCD1602(i2c, 2, 16)
d.display()
dht = DHT(18)

while True:
    temp,humid = dht.readTempHumid()#temp:  humid:
    sleep(1)
    d.clear()
    d.setCursor(0,0)
    d.print("Temp:"+str(temp))
    d.setCursor(0,1)
    d.print("Humid:"+str(humid))
    sleep(1)