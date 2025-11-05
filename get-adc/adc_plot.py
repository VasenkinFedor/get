import matplotlib.pyplot as plt

def plot_voltage_vs_time(time, voltage, max_voltage):
    plt.figure(figsize=(10, 6))
    plt.plot(time, voltage, 'b-', linewidth = 2, label='Напряжение')
    plt.title ('Зависимость напряжения от времени', fontsize = 14, fontweight='bold')
    plt.xlabel('Время (секунды)', fontsize=12)
    plt.ylabel('Напряжение (В)', fontsize=12)

    plt.xlim(0, max(time) if time else 1)
    plt.ylim(0, max_voltage*1.1)

    plt.grid(True, linestyle='--', alpha=0.7)

    plt.legend()

    plt.tight_layout()
    plt.show()

def plot_sampling_period_hist(time):
    sampling_periods = []

    for i in range(1, len(time)):
        period = time[i] - - time[i-1]
        sampling_periods.append(period)
    
    plt.figure(figsize=(10,6))
    plt.hist(sampling_periods)
    plt.title('завсимость напряжения от времени')
    plt.xlabel('время, с')
    plt.ylabel('напряжение, в')
    plt.xlim(0, 0.06)
    plt.grid(True)
    plt.show()