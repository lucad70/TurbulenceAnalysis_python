import math

AIR_DENSITY = 1.204  # kg/m³
AIR_VISCOSITY = 1.7894e-5  # kg/m.s

class ExperimentalProfile:
    def __init__(self, description):
        self.description = description
        self.position = []
        self.speed_profile = []
        self.turbulent_intensity_profile = []
        self.turbulent_kinetic_energy_profile = []

class ExperimentalData:
    def __init__(self, description, raw_time, raw_speed, typical_dimension):
        self.description = description
        self.raw_time = raw_time
        self.raw_speed = raw_speed
        self.typical_dimension = typical_dimension
        self.mean_average = 0.0
        self.fluctuation = []
        self.variance = 0.0
        self.standard_deviation = 0.0
        self.turbulent_kinetic_energy = 0.0
        self.turbulent_intensity = 0.0
        self.reynolds_number = 0.0
        self.coefficient_of_kurtosis = 0.0
        self.coefficient_of_skewness = 0.0
        self.density_of_probability = []

    

    def process(self):
        self.calculate_mean_average()
        self.calculate_fluctuation()
        self.calculate_variance()
        self.calculate_standard_deviation()
        self.calculate_turbulent_kinetic_energy()
        self.calculate_turbulent_intensity()
        self.calculate_coefficient_of_kurtosis()
        self.calculate_coefficient_of_skewness()
        self.calculate_reynolds_number()
        self.calculate_density_of_probability()

    def calculate_mean_average(self):
        self.mean_average = sum(self.raw_speed) / len(self.raw_speed)

    def calculate_fluctuation(self):
        self.fluctuation = [value - self.mean_average for value in self.raw_speed]

    def calculate_variance(self):
        self.variance = sum([(x - self.mean_average) ** 2 for x in self.raw_speed]) / len(self.raw_speed)

    def calculate_standard_deviation(self):
        self.standard_deviation = math.sqrt(self.variance)

    def calculate_turbulent_kinetic_energy(self):
        self.turbulent_kinetic_energy = 0.5 * self.variance

    def calculate_turbulent_intensity(self):
        self.turbulent_intensity = self.standard_deviation / abs(self.mean_average)

    def calculate_coefficient_of_kurtosis(self):
        numerator = sum([(x - self.mean_average) ** 4 for x in self.raw_speed]) / len(self.raw_speed)
        denominator = self.variance ** 2
        self.coefficient_of_kurtosis = numerator / denominator

    def calculate_coefficient_of_skewness(self):
        numerator = sum([(x - self.mean_average) ** 3 for x in self.raw_speed]) / len(self.raw_speed)
        denominator = self.variance ** 1.5
        self.coefficient_of_skewness = numerator / denominator

    def calculate_reynolds_number(self):
        self.reynolds_number = AIR_DENSITY * self.mean_average * self.typical_dimension / AIR_VISCOSITY

    def covariance(self, other):
        return sum([x * y for x, y in zip(self.fluctuation, other.fluctuation)]) / len(self.raw_speed)

    def correlation(self, other):
        return self.covariance(other) / (self.standard_deviation * other.standard_deviation)

    def density_of_probability_for_x(self, x):
        lambda_numerator = (x - self.mean_average) ** 2
        lambda_denominator = 2.0 * self.variance
        lambda_value = lambda_numerator / lambda_denominator
        denominator = self.standard_deviation * math.sqrt(2.0 * math.pi)
        probability = math.exp(-lambda_value) / denominator
        return probability

    def calculate_density_of_probability(self):
        probability_density = [self.density_of_probability_for_x(x) for x in self.raw_speed]
        self.density_of_probability = probability_density

def mean(numbers):
    return sum(numbers) / len(numbers)