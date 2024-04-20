import matplotlib
from output_fn import plot_density_probability, plot_raw_speed_time, plot_table
from processing_fn import probabilistic, temporal
from reading_fn import clean_subs_suffix, read_data, read_perf_files

def temporal_analysis(folder_path):
    dat_files = read_data(folder_path)
    processed_data = temporal(folder_path, dat_files)

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

def probabilistic_analysis(folder_path):
    dat_files = read_data(folder_path)
    processed_data = temporal(folder_path, dat_files)
    experimental_data_prob = probabilistic(processed_data)
    results = {
        "Mean Average": round(experimental_data_prob.mean_average, 2),
        "Variance": round(experimental_data_prob.variance, 2),
        "Standard Deviation": round(experimental_data_prob.standard_deviation, 2),
        "Turbulent Kinetic Energy": round(experimental_data_prob.turbulent_kinetic_energy, 2),
        "Turbulent Intensity": round(experimental_data_prob.turbulent_intensity, 2),
        "Reynolds Number": round(experimental_data_prob.reynolds_number, 2),
        "Coefficient of Kurtosis": round(experimental_data_prob.coefficient_of_kurtosis, 2),
        "Coefficient of Skewness": round(experimental_data_prob.coefficient_of_skewness, 2)
    }
    plot_table(results, 'High Reynolds Statistics Point 5')
    plot_density_probability(experimental_data_prob, 'probabilistic')
    plot_raw_speed_time(experimental_data_prob, 'probabilistic')
    
def profile_analysis(folder_path):
    dat_files = read_perf_files(folder_path)
    processed_data = temporal(folder_path, dat_files)

def temporal_main():
    folder_paths = ['data_from_experiment/re_temp/hre', 'data_from_experiment/re_temp/lre']
    for folder_path in folder_paths:
        temporal_analysis(folder_path)

def probabilistic_main():
    folder_paths = ['data_from_experiment/hre_prob']
    for folder_path in folder_paths:
        probabilistic_analysis(folder_path)

def profile_main():
    clean_subs_suffix('data_from_experiment/perfil/perfil_jus/PERFILM.W17')
    #folder_paths = ['data_from_experiment/perfil/perfil_jus', 'data_from_experiment/perfil/perfil_mon']
    #for folder_path in folder_paths:
    #    profile_analysis(folder_path)

def main():
    temporal_main()
    probabilistic_main()
    profile_main()

if __name__ == "__main__":
    # Call the main function for each program
    temporal_main()
    probabilistic_main()
    profile_main()
