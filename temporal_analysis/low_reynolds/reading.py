
from reading_fn import plot_density_probability, plot_raw_speed_time, plot_table, read_data


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
    folder_paths = ['data_from_experiment/re_temp/lre']
    for folder_path in folder_paths:
        main(folder_path)