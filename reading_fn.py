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

    return dat_files

