import unittest

from statistics_for_turbulence import ExperimentalData

class ExperimentalDataTests(unittest.TestCase):
    def setUp(self):
        # Set up the test data
        self.raw_data = [1.0, 2.0, 3.0, 4.0, 5.0]
        self.typical_dimension = 1.0
        self.raw_time = []
        self.data_processing = ExperimentalData("test", self.raw_time, self.raw_data.copy(), self.typical_dimension)
        self.data_processing.process()

    def test_mean_average(self):
        self.assertEqual(self.data_processing.mean_average, 3.0)

    def test_fluctuation(self):
        expected_fluctuation = [-2.0, -1.0, 0.0, 1.0, 2.0]
        self.assertEqual(self.data_processing.fluctuation, expected_fluctuation)

    def test_variance(self):
        self.assertEqual(self.data_processing.variance, 2.0)

    def test_standard_deviation(self):
        self.assertAlmostEqual(self.data_processing.standard_deviation, 1.4142135623730951)

    def test_turbulent_kinetic_energy(self):
        self.assertEqual(self.data_processing.turbulent_kinetic_energy, 1.0)

if __name__ == "__main__":
    unittest.main()