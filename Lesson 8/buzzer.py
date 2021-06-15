from machine import Pin, PWM
from time import sleep

buzzer = PWM(Pin(27))
while True:
    buzzer.freq(1046) #DO
    buzzer.duty_u16(1000)
    sleep(1)   
    buzzer.freq(1175) #RE
    buzzer.duty_u16(1000)
    sleep(1)        
    buzzer.freq(1318) #MI
    buzzer.duty_u16(1000)    
    sleep(1) 
    buzzer.freq(1397) #FA
    buzzer.duty_u16(1000)
    sleep(1) 
    buzzer.freq(1568) #SO
    buzzer.duty_u16(1000) 
    sleep(1)    
    buzzer.freq(1760) #LA
    buzzer.duty_u16(1000)   
    sleep(1)  
    buzzer.freq(1967) #SI
    buzzer.duty_u16(1000)
    sleep(1)