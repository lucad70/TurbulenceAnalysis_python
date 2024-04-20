import os
import pandas as pd
import sys
import numpy as np
from statistics_for_turbulence import ExperimentalData
from scipy.stats import linregress
import matplotlib.pyplot as plt

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
    plt.title(f'Experiment Results - {filename}')
    plt.savefig(f'images/tables/results_table_{filename}.png')
    plt.close()
    
def plot_density_probability(experimental_data, filename):
    """
    Plot density probability curves and save the image, comparing them with the corresponding Gaussian density probability distribution.

    Args:
    - experimental_data (ExperimentalData): ExperimentalData object.
    - filename (str): Name of the file for saving the plot.
    """
    mu = experimental_data.mean_average
    sigma = experimental_data.standard_deviation
    x = np.linspace(min(experimental_data.raw_speed), max(experimental_data.raw_speed), 100)
    y = (1 / (sigma * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x - mu) / sigma) ** 2)
    plt.plot(x, y, color='red', label='Gaussian Density of Probability')
    plt.hist(experimental_data.raw_speed, density=True, bins=20, alpha=0.5, label='Experimental Density of Probability')
    plt.title(f'Experiment Results - {filename} - Density of Probability')
    plt.legend()
    plt.savefig(f'images/plots/{filename}_density_probability_plot.png')
    plt.close()

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
    plt.title(f'Experiment Results - {filename} - Raw Speed vs Raw Time')
    plt.savefig(f'images/plots/{filename}_raw_speed_time_plot.png', dpi=300)
    plt.close()
