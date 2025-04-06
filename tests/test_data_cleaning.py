import unittest
import pandas as pd
from src import data_cleaning

class TestDataCleaning(unittest.TestCase):
    def setUp(self):
        self.df = pd.DataFrame({
            "Stone_Category": ["A", "B", "A", "B"],
            "pH_category": ["High", "Low", "High", "Low"],
            "Ca24": [100, 150, 120, 130],
            "SSCaP": [30, 35, 32, 31],
            "Ca24kg": [0.8, 0.9, 0.85, 0.87],
            "Ca24Cr24": [0.75, 0.8, 0.78, 0.76],
            "Cit24": [500, 520, 510, 515],
            "Serum_Ca": [9.5, 9.7, 9.6, 9.55],
            "Age": [45, 50, 38, 42],
            "BMI": [25, 28, 24, 26],
            "Same day sample pairs": [1, 1, 0, 1],
            "pH": [6.5, 7.0, 6.8, 7.1]
        })

    def test_clean_litholink_main(self):
        cleaned = data_cleaning.clean_litholink_main(self.df)
        expected_columns = {"Stone_Category", "pH_category", "Ca24", "SSCaP", "Ca24kg", "Ca24Cr24", "Cit24", "Serum_Ca", "Age", "BMI"}
        self.assertEqual(set(cleaned.columns), expected_columns)

    def test_clean_variability_study(self):
        cleaned = data_cleaning.clean_variability_study(self.df)
        expected_columns = {"Stone_Category", "Ca24", "SSCaP", "Ca24kg", "Ca24Cr24", "Cit24", "Serum_Ca", "pH"}
        self.assertEqual(set(cleaned.columns), expected_columns)

if __name__ == "__main__":
    unittest.main()
