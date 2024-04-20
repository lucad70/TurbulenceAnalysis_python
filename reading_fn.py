import os
import pandas as pd
import sys
import numpy as np
from output_fn import plot_density_probability, plot_raw_speed_time, plot_table
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

