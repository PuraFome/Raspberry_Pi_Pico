from machine import Pin
from time import sleep

## setup
led = Pin("LED", Pin.OUT)
count = 0

## loop
while True:
    led.toggle()
    sleep(1)
    count += 1
    print("Count = {}".format(count))