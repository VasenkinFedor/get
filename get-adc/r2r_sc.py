import time
from r2r_adc import R2R_ADC
from adc_plot import plot_voltage_vs_time

adc = R2R_ADC(dynamic_range=3.13, compare_time=0.01, verbose = False)

voltage_values = []
time_values = []

duration = 3.0


try: 
    start_time = time.time()


    while (time.time() - start_time) < duration:
        voltage_values.append(adc.get_sc_voltage())
        time_values.append(time.time()-start_time)
        time.sleep(0.05)

    plot_voltage_vs_time(time_values, voltage_values, adc.dynamic_range)
finally: 
    adc.cleanup()