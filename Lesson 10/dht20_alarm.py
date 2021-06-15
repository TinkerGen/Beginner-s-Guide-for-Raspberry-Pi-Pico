from lcd1602 import LCD1602
from dht20 import DHT20
from machine import I2C,Pin,ADC,PWM
from utime import sleep
i2c0 = I2C(0)#DHT20
i2c1 = I2C(1)#LCD
dht20 = DHT20(i2c0)
d = LCD1602(i2c1, 2, 16)
d.display()
buzzer = PWM(Pin(16))

while True:
    temper = dht20.dht20_temperature()
    humidity = dht20.dht20_humidity()
    sleep(1)
    d.clear()
    d.setCursor(0,0)
    d.print("Temp:"+str(temper))
    d.setCursor(0,1)
    d.print("Humid:"+str(humidity))
    sleep(1)
    
    if temper >30 or humidity <30:
        buzzer.freq(1000)
        buzzer.duty_u16(1000)
    else:
        buzzer.duty_u16(0)#close
