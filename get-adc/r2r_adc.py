import RPi.GPIO as GPIO
import time


maxVoltage = 255


class R2R_ADC:
    def __init__(self, dynamic_range, compare_time = 0.01, verbose = False):
        self.dynamic_range = dynamic_range
        self.verbose = verbose
        self.compare_time = compare_time
        
        self.bits_gpio = [26, 20, 19, 16, 13, 12, 25, 11]
        self.comp_gpio = 21

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.bits_gpio, GPIO.OUT, initial = 0)
        GPIO.setup(self.comp_gpio, GPIO.IN)

    def deinit(self):
        GPIO.output(self.bits_gpio, 0)
        GPIO.cleanup()

    def set_number(self, number):
        binary = [int(element) for element in bin(number)[2:].zfill(8)][::1]
        GPIO.output(self.bits_gpio, binary)

    def sequential_couting_adc(self):
        for value in range(1, 256):
            self.set_number(value)
            time.sleep(self.compare_time)
            comparatorValue = GPIO.input(self.comp_gpio)

            if comparatorValue == 0:
                return value - 1
        
        return maxVoltage

    def get_sc_voltage(self):
        digital_value = self.sequential_couting_adc()
        voltage = (digital_value / 255) * self.dynamic_range
        
        return voltage
    
    def successive_approximation_adc(self):
        result = 0

        for bit in range(7, -1, -1):
            test_value = result | (1 << bit)
            self.set_number(test_value)
            time.sleep(self.compare_time)

            comparator_value = GPIO.input(self.comp_gpio)

            if comparator_value == 1:
                result = test_value
            
            return result
    
    def get_sar_voltage(self):
        digital_value = self.successive_approximation_adc()
        voltage = digital_value*self.dynamic_range/255

        return voltage
'''
if __name__ == "__main__":
    try:
        adc = R2R_ADC(3.281)

        while True:
            voltage = adc.get_sc_voltage()
            print(voltage)
            time.sleep(1)
        
    finally:
        adc.deinit()
'''

if __name__ == "__main__":
    try:
        adc = R2R_ADC(3.281)

        while True:
            voltage = adc.get_sar_voltage()
            print(voltage)
            time.sleep(1)
    
    finally:
        adc.deinit()