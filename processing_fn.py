import os
import pandas as pd
from statistics_for_turbulence import ExperimentalData

def process_data(folder_path, dat_files):
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

