import os
import pandas as pd
import sys
import numpy as np
from output_fn import plot_density_probability, plot_raw_speed_time, plot_table
from statistics_for_turbulence import ExperimentalData
from scipy.stats import linregress
import matplotlib.pyplot as plt

def read_data(folder_path):
    dat_files = [file for file in os.listdir(folder_path) if file.endswith('.dat')]
    return dat_files

def read_perf_files(folder_path):
    for files in folder_path: clean_subs_suffix(folder_path)
    dat_files = [file for file in os.listdir(folder_path) if file.endswith('.dat')]
    return dat_files

def clean_subs_suffix(file):
    file_name, file_extension = os.path.splitext(file)
    new_file_name = file_name.replace('.', '_') + '.dat'
    return new_file_name