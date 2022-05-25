import board
import digitalio
import time

led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

print("NAH gulpfile.js is WAY better!")

while True:
    led.value = True
    time.sleep(1)
    led.value = False
    time.sleep(1)
