import os
import pandas as pd
import sys
from statistics_for_turbulence import ExperimentalData
import numpy as np
from scipy.stats import linregress

sys.path.append("..")
import matplotlib.pyplot as plt

# Define the folder path
folder_path = 'data_from_experiment/re_temp/hre'

# Get a list of all .dat files in the folder
dat_files = [file for file in os.listdir(folder_path) if file.endswith('.dat')]

# Loop through each .dat file
for file in dat_files:
    # Define the file path
    file_path = os.path.join(folder_path, file)

    # Read the file using pandas
    data = pd.read_csv(file_path, delimiter='\s+', header=None)

    # Extract the columns into separate variables
    time = data[0].tolist()
    speed_inst = data[1].tolist()
    typical_dimension = 0.05

    # Create an instance of the ExperimentalData class
    experimental_data = ExperimentalData(file, time, speed_inst, typical_dimension)
    experimental_data.process()

    # Print the results as a table
    results = {
        "Mean Average": round(experimental_data.mean_average, 2),
        "Variance": round(experimental_data.variance, 2),
        "Standard Deviation": round(experimental_data.standard_deviation, 2),
        "Turbulent Kinetic Energy": round(experimental_data.turbulent_kinetic_energy, 2),
        "Turbulent Intensity": round(experimental_data.turbulent_intensity, 2),
        "Reynolds Number": round(experimental_data.reynolds_number, 2),
        "Coefficient of Kurtosis": round(experimental_data.coefficient_of_kurtosis, 2),
        "Coefficient of Skewness": round(experimental_data.coefficient_of_skewness, 2)
    }

    df = pd.DataFrame(results.items(), columns=["Parameter", "Value"])

    # Plot the table as an image
    fig, ax = plt.subplots(figsize=(8, 4))
    ax.axis('off')
    ax.axis('tight')
    ax.table(cellText=df.values, colLabels=df.columns, loc='center')
    plt.title(f'High Reynolds Experiment Results - {file}')
    plt.savefig(f'images/tables/results_table_{file}.png')
    plt.show()

    # Calculate the Gaussian density of probability
    mu = experimental_data.mean_average
    sigma = experimental_data.standard_deviation
    x = np.linspace(min(experimental_data.raw_speed), max(experimental_data.raw_speed), 100)
    y = (1 / (sigma * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x - mu) / sigma) ** 2)

    # Plot the Gaussian density of probability
    plt.plot(x, y, color='red', label='Density of Probability')
    plt.title(f'High Reynolds Experiment Results - {file} - Density of Probability')
    plt.legend()

    # Save the plot image
    plt.savefig(f'images/plots/{file}_density_probability_plot.png')

    plt.show()


    # Create a scatter plot of raw_time vs raw_speed
    plt.plot(experimental_data.raw_time, experimental_data.raw_speed)
    plt.xlabel('Time')
    plt.ylabel('Speed')
    plt.title(f'High Reynolds Experiment Results - {file} - Raw Speed vs Raw Time')

    # Save the plot image with higher resolution
    plt.savefig(f'images/plots/{file}_raw_speed_time_plot.png', dpi=300)

    plt.show()

