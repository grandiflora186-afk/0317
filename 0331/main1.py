from time import sleep
from machine import Pin

led=Pin(5,Pin.OUT)
led2=Pin(9,Pin.OUT)


# 입력함수를 사용해서 '1' : led 켜지고, '0' 일 때 led 꺼지도록 설정
from time import sleep
from machine import Pin

led=Pin(5,Pin.OUT)
led2=Pin(9,Pin.OUT)

while True:
    n = input()
    print(n)
    if n == '1':
        print("LED ON")
        led.value(1) #Set led turn on
        sleep(1)
    else:
        led.value(0) #Set led turn off
