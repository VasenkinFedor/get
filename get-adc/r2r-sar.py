from matplotlib import pyplot as plt
import time, r2r_adc, adc_plot

adc = r2r_adc.R2R_ADC(3.281)

voltage_values = []
time_values = []
duration = 3.0

try:
    start_time = time.time()

    while(time.time() - start_time < duration):
        voltage_values.append(adc.get_sar_voltage())
        time_values.append(time.time() - start_time)
    
    adc_plot.plot_voltage_vs_time(time_values, voltage_values, 3.5)
    adc_plot.plot_sampling_period_hist(time_values)

finally:
    adc.deinit()