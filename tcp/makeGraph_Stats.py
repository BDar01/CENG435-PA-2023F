import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator

def read_times_from_file(file_name):
    times_list = []
    with open(file_name, 'r') as file:
        for line in file:
            if line.startswith("Time"):
                time_value = float(line.split(":")[1].strip()[:-1])
                times_list.append(time_value)

    # Calculate mean and confidence interval
    mean_value = np.mean(times_list)
    std_err = stats.sem(times_list)
    dof = len(times_list) - 1
    confidence_interval = stats.t.interval(0.95, dof, loc=mean_value, scale=std_err)
    max_value = max(times_list)
    min_value = min(times_list)

    # Append mean and confidence interval to the end of the file
    with open(file_name, 'a') as file:
        file.write(f"\n\nMax: {max_value}\n")
        file.write(f"Min: {min_value}\n")
        file.write(f"Mean: {mean_value}\n")
        file.write(f"Confidence Interval: {confidence_interval}")

    return times_list

def create_plot(times_list, file_name):
    fig, ax = plt.subplots(figsize=(10, 6))  # Set the figure size here
    ax.plot(range(1, len(times_list) + 1), times_list, label="Time per run")
    ax.set_xticks(range(1, len(times_list) + 1))
    ax.yaxis.set_major_locator(MaxNLocator(prune='both'))  # Adjust y-axis ticks
    ax.set_xlabel("Run")
    ax.set_ylabel("Time (s)")
    ax.legend()
    ax.set_title("TCP with 100ms Delay (Uniform Dist.)")
    fig.savefig(f"{file_name}_figure.png")

def main():
    file_name = input("Enter the file name: ")
    times_list = read_times_from_file(file_name)
    create_plot(times_list, file_name)

if __name__ == "__main__":
    main()
