from machine import Pin, PWM
import time

led = [PWM(Pin(18, mode=Pin.OUT)), PWM(Pin(17, mode=Pin.OUT)), PWM(Pin(16, mode=Pin.OUT))]
# led[0] = rouge
# led[1] = vert
# led[2] = bleu

def reset():
    for i in led:
        i.freq(1000)
        i.duty_u16(0)

def violet():
    reset()
    led[0].duty_u16(20000)
    led[2].duty_u16(20000)

def blanc():
    for i in led:
        i.freq(1000)
        i.duty_u16(20000)
        
def setColor(r,v,b):
    c = [r,v,b]
    for i in range(3):
        led[i].duty_u16(c[i]*256)