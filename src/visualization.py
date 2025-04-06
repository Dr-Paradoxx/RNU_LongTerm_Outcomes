"""
Module: visualization
Provides functions to generate professional plots for the RNU project.
"""

import matplotlib.pyplot as plt
import pandas as pd

def plot_variable_distribution(df: pd.DataFrame, variable: str, output_path: str = None):
    """
    Generates a boxplot for the specified variable across stone categories.
    """
    categories = df["Stone_Category"].unique()
    data = [df[df["Stone_Category"] == cat][variable] for cat in categories]
    plt.figure(figsize=(8, 6))
    plt.boxplot(data, labels=categories)
    plt.title(f"Distribution of {variable} by Stone Category")
    plt.xlabel("Stone Category")
    plt.ylabel(variable)
    plt.tight_layout()
    if output_path:
        plt.savefig(output_path)
    else:
        plt.show()
    plt.close()

def plot_variability_bar(df: pd.DataFrame, variable: str, output_path: str = None):
    """
    Generates a bar chart showing the mean values of the variable by stone category.
    """
    means = df.groupby("Stone_Category")[variable].mean()
    plt.figure(figsize=(8, 6))
    plt.bar(means.index, means.values)
    plt.title(f"Mean {variable} by Stone Category")
    plt.xlabel("Stone Category")
    plt.ylabel(f"Mean {variable}")
    plt.tight_layout()
    if output_path:
        plt.savefig(output_path)
    else:
        plt.show()
    plt.close()
