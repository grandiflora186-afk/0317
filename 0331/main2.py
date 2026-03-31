from machine import Pin
import time

led=Pin(5 ,Pin.OUT)
button_pin = Pin(7, Pin.IN, Pin.PULL_UP)

led_push = 0

while True:
    if button_pin.value() == 0:
        if led_push == 0:
            led_push = 1
        else:
            led_push = 0

        print("Button Pressed!")
        time.sleep(0.2)

    else:
        print("Button OFF!")

    led.value(led_push)
    time.sleep(0.05)