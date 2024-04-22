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
    plt.plot(x, y, color='red', label='Densidade de Probabilidade')
    sigma_normal = 1
    y_normal = (1 / (sigma_normal * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x - mu) / sigma_normal) ** 2)
    plt.plot(x, y_normal, color = 'green', label = 'Densidade Gaussiana Normal')
    plt.hist(experimental_data.raw_speed, density=True, bins=20, alpha=0.5, label='Experimental Density of Probability')
    plt.xlabel('Velocidade (m/s)')
    plt.ylabel('Contagem')
    plt.title(f'Resultados Experimentais - {filename} - Densidade de Probabilidade')
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
    plt.xlabel('Tempo (s)')
    plt.ylabel('Velocidade (m/s)')
    plt.title(f'EResultados Experimentais - {filename} - Tempo vs Velocidade')
    plt.savefig(f'images/plots/{filename}_raw_speed_time_plot.png', dpi=300)
    plt.close()

def plot_profile_speed(speed, z_positions, description):
    """
    Plot speed profile and save the image.

    Args:
    - speed (list): List of speeds.
    - z_positions (list): List of z positions.
    - folder_path (str): Folder path.
    """
    plt.plot(speed, z_positions)
    plt.scatter(speed, z_positions)
    plt.xlabel('Velocidade (m/s)')
    plt.ylabel('Altura z (cm)')
    plt.title(f'Resultados Experimentais - {description} - Perfil de Velocidade')
    plt.savefig(f'images/plots/{description}_speed_profile_plot.png')
    plt.close()

def plot_profile_turbulent_intensity(turbulent_intensity, z_positions, description):
    """
    Plot turbulent intensity profile and save the image.

    Args:
    - turbulent_intensity (list): List of turbulent intensities.
    - z_positions (list): List of z positions.
    - folder_path (str): Folder path.
    """
    plt.scatter(turbulent_intensity, z_positions)
    plt.plot(turbulent_intensity, z_positions)
    plt.xlabel('Intensidade Turbulenta (%)')
    plt.ylabel('Altura em z (cm)')
    plt.title(f'Resultados Experimentais - {description} - Perfil de Intensidade Turbulenta')
    plt.savefig(f'images/plots/{description}_turbulent_intensity_profile_plot.png')
    plt.close()