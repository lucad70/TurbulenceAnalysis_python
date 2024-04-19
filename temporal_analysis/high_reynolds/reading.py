import pandas as pd
import sys
sys.path.append("..")
from statistics_for_turbulence import ExperimentalData
import numpy as np
from scipy.stats import linregress
import pandas as pd

# Define the file path
file_path = 'data_from_experiment/re_temp/hre/hre1.dat'

# Read the file using pandas
data = pd.read_csv(file_path, delimiter='\s+', header=None)

# Extract the columns into separate variables
time = data[0].tolist()
speed_inst = data[1].tolist()
typical_dimension = 0.05

# Create an instance of the ExperimentalData class
hre1 = ExperimentalData("HRE1", time, speed_inst, typical_dimension)
hre1.process()

# Print the results as a table
import matplotlib.pyplot as plt

results = {
    "Mean Average": round(hre1.mean_average, 2),
    "Variance": round(hre1.variance, 2),
    "Standard Deviation": round(hre1.standard_deviation, 2),
    "Turbulent Kinetic Energy": round(hre1.turbulent_kinetic_energy, 2),
    "Turbulent Intensity": round(hre1.turbulent_intensity, 2),
    "Reynolds Number": round(hre1.reynolds_number, 2),
    "Coefficient of Kurtosis": round(hre1.coefficient_of_kurtosis, 2),
    "Coefficient of Skewness": round(hre1.coefficient_of_skewness, 2)
}

df = pd.DataFrame(results.items(), columns=["Parameter", "Value"])

# Plot the table as an image
fig, ax = plt.subplots(figsize=(8, 4))
ax.axis('off')
ax.axis('tight')
ax.table(cellText=df.values, colLabels=df.columns, loc='center')
plt.title('Results')
plt.savefig('results_table.png')
plt.show()

import matplotlib.pyplot as plt

# Create a scatter plot of speed vs density probability
plt.scatter(hre1.raw_speed, hre1.density_of_probability)
plt.xlabel('Speed')
plt.ylabel('Density Probability')
plt.title('Density Probability vs Speed')

# Calculate the Gaussian density of probability
mu = hre1.mean_average
sigma = hre1.standard_deviation
x = np.linspace(min(hre1.raw_speed), max(hre1.raw_speed), 100)
y = (1 / (sigma * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x - mu) / sigma) ** 2)

# Plot the Gaussian density of probability
plt.plot(x, y, color='red', label='Density of Probability')

plt.legend()

plt.show()