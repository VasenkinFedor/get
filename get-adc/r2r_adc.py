import RPi.GPIO as GPIO
import time 
class R2R_ADC:
    def __init__(self, dynamic_range, compare_time = 0.02, verbose = False):
        self.dynamic_range = dynamic_range
        self.verbose = verbose
        self.compare_time = compare_time
        
        self.bits_gpio = [26, 20, 19, 16, 13, 12, 25, 11]
        self.comp_gpio = 21

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.bits_gpio, GPIO.OUT, initial = 0)
        GPIO.setup(self.comp_gpio, GPIO.IN)

    def number_to_dac(self, number):
        if number <0 or number > 255:
            raise ValueError(f"Число {number} вне диапазона 0-255 для 8-битного ЦАП")
        binary_str = format(number, '08b')

        if self.verbose:
            print(f"R2R_ADC: Подаем число {number} (бинарно: {binary_str})) на ЦАП")

        for i, pin in enumerate(self.bits_gpio):
            bit_value = int(binary_str[i])
            GPIO.output(pin, bit_value)
                
                
               
    def sequential_couting_adc(self):
        if self.verbose:
            print("R2R_ADC: Запуск последовательного преобразования АЦП")

        max_number = 255

        for number in range(max_number + 1):
            self.number_to_dac(number)

            time.sleep(self.compare_time)

            comparator_state = GPIO.input(self.comp_gpio)

            if self.verbose: 
                voltage_dac = (number / max_number) * self.dynamic_range
                print(f"Число {number}, Напряжение ЦАП: {voltage_dac:.2f}В, Компаратор: {comparator_state}")
            if comparator_state == GPIO.HIGH:
                if self.verbose:
                    print(f"Число {number}, Напряжение на ЦАП: {voltage_dac:.2f}В, Компаратор: {comparator_state}")
                return number
                    
        if self.verbose:
           print(f"R2R_ADC: Превышение не достигнуто. Возвращаем максимум: {max_number}")
        return max_number


    def get_sc_voltage(self):
        digital_value = self.sequential_couting_adc()
        voltage = (digital_value / 255) * self.dynamic_range
        
        if self.verbose:
            print(f"R2R_ADC: Цифровое значение: {digital_value}, Напряжение: {voltage:.3f}В")

        return voltage
    def __del__(self):

        try:
            for pin in self.bits_gpio:
                GPIO.output(pin, GPIO.LOW)

            GPIO.cleanup()

            if self.verbose:
                print("R2R_ADC: GPIO очищен")
        except Exception as e:
            if self.verbose:
                print(f"R2R_ADC: Ошибка при очистке: {e}")



if __name__ == "__main__":
    try:
        adc=R2R_ADC(dynamic_range=3.13   , compare_time=0.01, verbose=False)
        while True:
            try:
                voltage = adc.get_sc_voltage()
                print(f"Напряжение: {voltage:.3f} В") 
                time.sleep(0.5)
            except KeyboardInterrupt:
                print("\nПрерывание пользователем")
                break
    except Exception as e:
        print(f"Ошибка: {e}")
    finally:
        if 'adc' in locals():
            adc.__del__()