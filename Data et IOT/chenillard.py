from machine import Pin
import utime

pinNumber = 14
led = Pin(pinNumber, mode = Pin.OUT)
led2 = Pin(10, mode = Pin.OUT)
led3 = Pin(6, mode = Pin.OUT)
led4 = Pin(2, mode = Pin.OUT)
time = 0.1
led.off()
led2.off()
led3.off()
led4.off()

while True:
    led.toggle()
    utime.sleep(time)
    led.toggle()
    led2.toggle()
    utime.sleep(time)
    led2.toggle()
    led3.toggle()
    utime.sleep(time)
    led3.toggle()
    led4.toggle()
    utime.sleep(time)
    led4.toggle()
    led3.toggle()
    utime.sleep(time)
    led3.toggle()
    led2.toggle()
    utime.sleep(time)
    led2.toggle()