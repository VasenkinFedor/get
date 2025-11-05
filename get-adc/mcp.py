import time, matplotlib.pyplot as plt
from mcp3021_driver import MCP3021

adc = MCP3021(dynamic_range = 5.0, verbose = False)

voltages = []
time_points = []

duration = 10

try:
    start_time = time.time()

    while time.time() - start_time < duration:
        voltage = adc.get_voltage()
        voltages.append(voltage)
        time_points.append(time.time() - start_time)

        time.sleep(0.1)
    
    plt.figure(figsize=(10, 6))
    plt.plot(time_points, voltages, 'b-', linewidth=2)
    plt.title('измерение напряжения')
    plt.xlabel('время, с')
    plt.ylabel('напряжение, В')
    plt.grid(True)

    plt.show()

finally:
    adc.deinit()