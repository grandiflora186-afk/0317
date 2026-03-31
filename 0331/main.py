from time import sleep
from machine import Pin
#create LED object from pin2,Set Pin2 to output
led=Pin(2,Pin.OUT)
while True:
    led.value(0) #Set led turn on
    sleep(1)
    led.value(1) #Set led turn off
    sleep(1)