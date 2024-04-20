import os
import pandas as pd
import sys
import numpy as np
from statistics_for_turbulence import ExperimentalData
from scipy.stats import linregress
import matplotlib.pyplot as plt

def read_data(folder_path):
    """
    Read data from .dat files in the specified folder.

    Args:
    - folder_path (str): Path to the folder containing .dat files.

    Returns:
    - dict: Dictionary containing ExperimentalData objects with filenames as keys.
    """
    dat_files = [file for file in os.listdir(folder_path) if file.endswith('.dat')]
    processed_data = {}
    
    for file in dat_files:
        file_path = os.path.join(folder_path, file)
        data = pd.read_csv(file_path, delimiter='\s+', header=None)
        time = data[0].tolist()
        speed_inst = data[1].tolist()
        typical_dimension = 0.05
        experimental_data = ExperimentalData(file, time, speed_inst, typical_dimension)
        experimental_data.process()
        processed_data[file] = experimental_data
    
    return processed_data

def plot_table(results, filename):
    """
    Plot the results as a table and save the image.

    Args:
    - results (dict): Dictionary containing results to be plotted.
    - filename (str): Name of the file for saving the plot.
    """
    df = pd.DataFrame(results.items(), columns=["Parameter", "Value"])
    fig, ax = plt.subplots(figsize=(8, 4))
    ax.axis('off')
    ax.axis('tight')
    ax.table(cellText=df.values, colLabels=df.columns, loc='center')
    plt.title(f'High Reynolds Experiment Results - {filename}')
    plt.savefig(f'images/tables/results_table_{filename}.png')
    plt.show()

def plot_density_probability(experimental_data, filename):
    """
    Plot Gaussian density of probability and save the image.

    Args:
    - experimental_data (ExperimentalData): ExperimentalData object.
    - filename (str): Name of the file for saving the plot.
    """
    mu = experimental_data.mean_average
    sigma = experimental_data.standard_deviation
    x = np.linspace(min(experimental_data.raw_speed), max(experimental_data.raw_speed), 100)
    y = (1 / (sigma * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x - mu) / sigma) ** 2)
    plt.plot(x, y, color='red', label='Density of Probability')
    plt.title(f'High Reynolds Experiment Results - {filename} - Density of Probability')
    plt.legend()
    plt.savefig(f'images/plots/{filename}_density_probability_plot.png')
    plt.show()

def plot_raw_speed_time(experimental_data, filename):
    """
    Plot raw_time vs raw_speed and save the image.

    Args:
    - experimental_data (ExperimentalData): ExperimentalData object.
    - filename (str): Name of the file for saving the plot.
    """
    plt.plot(experimental_data.raw_time, experimental_data.raw_speed)
    plt.xlabel('Time')
    plt.ylabel('Speed')
    plt.title(f'High Reynolds Experiment Results - {filename} - Raw Speed vs Raw Time')
    plt.savefig(f'images/plots/{filename}_raw_speed_time_plot.png', dpi=300)
    plt.show()

def main(folder_path):
    processed_data = read_data(folder_path)

    for file, experimental_data in processed_data.items():
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
        plot_table(results, file)
        plot_density_probability(experimental_data, file)
        plot_raw_speed_time(experimental_data, file)

if __name__ == "__main__":
    # Call the main function for each program
    folder_paths = ['data_from_experiment/re_temp/hre']
    for folder_path in folder_paths:
        main(folder_path)
