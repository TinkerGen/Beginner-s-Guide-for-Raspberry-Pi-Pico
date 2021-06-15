import machine
import utime
button = machine.Pin(18, machine.Pin.IN)
miniFan = machine.Pin(16, machine.Pin.OUT)
val = 0
while True:
    val = button.value()
    if val == 1:
        miniFan.toggle()
        utime.sleep_ms(100)