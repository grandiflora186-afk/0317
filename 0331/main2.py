from machine import Pin
import time

led=Pin(5 ,Pin.OUT)
button_pin = Pin(7, Pin.IN, Pin.PULL_UP)

flag = 0

while True:
    if button_pin.value() == 0:
        if flag == 0:
            flag = 1
        else:
            flag = 0

        print("Button Pressed!")
        time.sleep(0.2)

    else:
        print("Button OFF!")

    led.value(flag)
    time.sleep(0.05)