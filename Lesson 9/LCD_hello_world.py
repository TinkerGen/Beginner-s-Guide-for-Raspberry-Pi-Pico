from lcd1602 import LCD1602
from machine import I2C,Pin
from utime import sleep
i2c = I2C(1,scl=Pin(7), sda=Pin(6), freq=400000)
d = LCD1602(i2c, 2, 16) #标注数据类型，行数和每一行的字符数

d.display() #启动显示屏
sleep(1)
d.clear() #清理显示
d.print('Hello ') #显示字符

sleep(1)
d.setCursor(0, 1) #规定显示位置，行和列都从0开始
d.print('world ')