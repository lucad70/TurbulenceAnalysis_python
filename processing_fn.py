import os
import pandas as pd
from statistics_for_turbulence import ExperimentalData, ExperimentalProfile, mean

def temporal(folder_path, dat_files):
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

def probabilistic(processed_data):
    first_experimental_data = list(processed_data.values())[0]
    raw_speed = []
    raw_time = first_experimental_data.raw_time
    description = 'Probabilistic'
    typical_dimension = 0.05
    experimental_data_prob = ExperimentalData(description, raw_time, raw_speed, typical_dimension)
    instant_speed = []

    for file, experimental_data in processed_data.items():
        instant_speed.append(experimental_data.raw_speed)
    
    grouped_elements = zip(*instant_speed)
    statistical_speed = [mean(group) for group in grouped_elements]
    experimental_data_prob.raw_speed = statistical_speed
    
    experimental_data_prob.process()
    return experimental_data_prob

def profile(processed_data,folder_path):
    first_experimental_data = list(processed_data.values())[0]
    z_positions = []
    speeds = []
    kinetic_energies = []
    turbulent_intensities = []

    for file, experimental_data in processed_data.items():
        speeds.append(experimental_data.mean_average)
        kinetic_energies.append(experimental_data.turbulent_kinetic_energy)
        turbulent_intensities.append(experimental_data.turbulent_intensity)

    experiment_profile = ExperimentalProfile(folder_path, z_positions, speeds, kinetic_energies, turbulent_intensities)