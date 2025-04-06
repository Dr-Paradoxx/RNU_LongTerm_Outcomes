"""
Module: data_cleaning
Provides functions to load, clean, and save clinical data for the RNU project.
"""

import pandas as pd
import os

def load_excel_data(filepath: str) -> dict:
    """
    Loads an Excel file and returns a dictionary of DataFrames keyed by sheet name.
    """
    try:
        sheets = pd.read_excel(filepath, sheet_name=None, engine="openpyxl")
        return sheets
    except Exception as e:
        raise IOError(f"Error loading Excel file: {e}")

def clean_litholink_main(df: pd.DataFrame) -> pd.DataFrame:
    """
    Cleans the Litholink_main sheet by selecting relevant columns and dropping missing values.
    """
    columns = ['Stone_Category', 'pH_category', 'Ca24', 'SSCaP', 'Ca24kg', 'Ca24Cr24', 'Cit24', 'Serum_Ca', 'Age', 'BMI']
    df_clean = df[columns].copy()
    df_clean.dropna(inplace=True)
    return df_clean

def clean_variability_study(df: pd.DataFrame) -> pd.DataFrame:
    """
    Cleans the Variability Study sheet by filtering same-day sample pairs and selecting relevant columns.
    """
    df_clean = df[df["Same day sample pairs"] == 1].copy()
    columns = ['Stone_Category', 'Ca24', 'SSCaP', 'Ca24kg', 'Ca24Cr24', 'Cit24', 'Serum_Ca', 'pH']
    df_clean = df_clean[columns]
    df_clean.dropna(inplace=True)
    return df_clean

def save_processed_data(df: pd.DataFrame, output_path: str):
    """
    Saves the DataFrame to CSV at the given output path.
    """
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df.to_csv(output_path, index=False)
