import pandas as pd
import sys
sys.path.append("..")
from statistics_for_turbulence import ExperimentalData

# Define the file path
file_path = 'data_from_experiment/re_temp/hre/hre1.dat'

# Read the file using pandas
data = pd.read_csv(file_path, delimiter='\s+', header=None)

# Extract the columns into separate variables
time = data[0].tolist()
speed_inst = data[1].tolist()

# Create an instance of the ExperimentalData class
hre1 = ExperimentalData("HRE1", time, speed_inst, 0.1)
hre1.process()

