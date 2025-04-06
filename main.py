"""
Entry-point for RNU Long-Term Outcomes Analysis.
"""

import os
from src import data_cleaning, analysis, visualization, survival_analysis

def main():
    print("Starting RNU Long-Term Outcomes Analysis...")
    # Example path to raw data (update with actual file path if needed)
    raw_data_path = os.path.join("data", "raw", "Robotic_NephU_Database.xlsx")
    
    try:
        # Load data from Excel file
        sheets = data_cleaning.load_excel_data(raw_data_path)
        if "Litholink_main" in sheets:
            main_df = data_cleaning.clean_litholink_main(sheets["Litholink_main"])
            print("Cleaned Litholink_main data (first 5 rows):")
            print(main_df.head())
            # Perform statistical analysis
            results = analysis.analyze_stone_and_ph_impact(main_df)
            print("Statistical Analysis Results:")
            for key, value in results.items():
                print(f"{key}: {value}")
            # Generate a sample visualization (e.g., boxplot for 'Ca24')
            visualization.plot_variable_distribution(main_df, "Ca24", output_path="plots/Ca24_boxplot.png")
        else:
            print("Sheet 'Litholink_main' not found in the Excel file.")
    except Exception as e:
        print(f"An error occurred: {e}")
    
    # Note: Add further survival analysis or additional steps as needed.

if __name__ == "__main__":
    main()
