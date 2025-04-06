"""
Module: analysis
Provides statistical analysis functions for the RNU project.
"""

import pandas as pd
import scipy.stats as stats

def analyze_stone_and_ph_impact(df: pd.DataFrame) -> dict:
    """
    Performs statistical tests (e.g., Kruskal-Wallis) to assess the impact of stone and pH categories.
    Returns a dictionary with test statistics and p-values.
    """
    results = {}
    variables = ['Ca24', 'SSCaP', 'Ca24kg', 'Ca24Cr24', 'Cit24', 'Serum_Ca']
    grouped = df.groupby(["Stone_Category", "pH_category"])
    for var in variables:
        try:
            groups = [group[var].values for name, group in grouped]
            stat, p_value = stats.kruskal(*groups)
            results[var] = {"statistic": stat, "p_value": p_value}
        except Exception as e:
            results[var] = {"error": str(e)}
    return results

def analyze_variability(df: pd.DataFrame) -> dict:
    """
    Calculates variability (standard deviation) for selected variables by stone category.
    """
    variability_results = {}
    variables = ['Ca24', 'SSCaP', 'Ca24kg', 'Ca24Cr24', 'Cit24', 'Serum_Ca', 'pH']
    for var in variables:
        variability = df.groupby("Stone_Category")[var].std()
        variability_results[var] = variability.to_dict()
    return variability_results
