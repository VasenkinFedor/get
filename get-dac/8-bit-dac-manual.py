import RPi.GPIO as GPIO
import time 
GPIO.setmode(GPIO.BCM)
dac_pins=[16,20,21,25,26,17,27,22]
for pin in dac_pins:
    GPIO.setup(pin, GPIO.OUT)
dynamic_range = 3.3

def voltage_to_number(voltage):
    if not (0.0 <= voltage <= dynamic_range):
        print(f"Напряжение выходит за динамический диапазон ЦАП (0.00 - {dynamic_range:.2f} В)")
        print("Устанавлниваем 0.0 В")
        return 0

    return int(voltage / dynamic_range * 255)

def number_to_dac(value):
    return[int (element) for element in bin(value)[2:].zfill(8)]

try:
    while True:
        try:
            voltage = float(input("Введите напряжение в Вольтах: "))
            number = voltage_to_number(voltage)
            binary_array = number_to_dac(number)
            print(f"число на вход ЦАП:{number}, биты:{binary_array}")
            GPIO.output(dac_pins, binary_array)
        except ValueError:
            print("Вы ввели не число. Попробуйте ещё раз\n")

finally:
    GPIO.output(dac_bits, 0)
    GPIO.cleanup()