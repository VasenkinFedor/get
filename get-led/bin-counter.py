import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
leds = [16, 12, 25, 17, 27, 23, 22, 24]
for pin in leds:
    GPIO.setup(pin, GPIO.OUT)
for pin in leds:
    GPIO.output(pin, GPIO.LOW)
up = 9
down = 10
GPIO.setup(up, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(down, GPIO.IN, pull_up_down=GPIO.PUD_UP)
num=0
def dec2bin(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]
sleep_time = 0.2
try:
    while True:
        if GPIO.input(up) == GPIO.LOW:
            if num<255:
                num+=1
                binary= dec2bin(num)
                for i in range(8):
                    GPIO.output(leds[i], binary[i])
                time.sleep(sleep_time)
        if GPIO.input(down) == GPIO.LOW:
            if num > 0:
                num-=1
                binary = dec2bin(num)
                for i in range(8):
                    GPIO.output(leds[i], binary[i])
                time.sleep(sleep_time)
        time.sleep(0.005)
finally:
    for pin in leds:
        GPIO.output(pin, GPIO.LOW)
    GPIO.cleanup()