from lcd1602 import LCD1602
from dht20 import DHT20
from machine import I2C,Pin,ADC
from utime import sleep

i2c0 = I2C(0)#DHT20
i2c1 = I2C(1)#LCD
dht20 = DHT20(i2c0)
d = LCD1602(i2c1, 2, 16)
d.display()

miniFan = machine.Pin(18,machine.Pin.OUT)

while True:
    temper = dht20.dht20_temperature()  
    sleep(1)
    d.clear()
    d.setCursor(0,0)
    d.print("Temp:"+str(temper))
    sleep(1)
    if temper > 26:
        miniFan.value(1)
    else:
        miniFan.value(0)