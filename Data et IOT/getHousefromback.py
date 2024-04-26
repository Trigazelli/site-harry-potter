import network   #import des fonction lier au wifi
import urequests	#import des fonction lier au requetes http
import utime	#import des fonction lier au temps
import ujson	#import des fonction lier aà la convertion en Json
from machine import Pin, PWM
import time

led = [PWM(Pin(18, mode=Pin.OUT)), PWM(Pin(17, mode=Pin.OUT)), PWM(Pin(16, mode=Pin.OUT))]
# led[0] = rouge
# led[1] = vert
# led[2] = bleu

wlan = network.WLAN(network.STA_IF) # met la raspi en mode client wifi
wlan.active(True) # active le mode client wifi

ssid = 'Banane'
password = 'alexandre'
wlan.connect(ssid, password) # connecte la raspi au réseau
perso = "quirinus-quirrel"
url = "http://192.168.146.86:3000/house"

while not wlan.isconnected():
    print("pas co")
    utime.sleep(1)
    pass

def setColor(c):
    for i in range(3):
        led[i].duty_u16(c[i]*256)
        
def reset():
    for i in led:
        i.freq(1000)
        i.duty_u16(0)
        
maison = {
"Gryffindor": [255,0,0],
"Hufflepuff": [200,200,0],
"Ravenclaw": [0,0,255],
"Slytherin":[0,255,0]}

while(True):
    try:
        print("GET")
        r = urequests.get(url) # lance une requete sur l'url
        print(r.json())
        setColor(maison[r.json()["house"]]) # traite sa reponse en Json
        r.close() # ferme la demande
        utime.sleep(1)  
    except Exception as e:
        print(e)
        
        
        