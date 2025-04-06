"""
Module: survival_analysis
Provides functions for Kaplan-Meier survival analysis using the lifelines package.
"""

import pandas as pd
from lifelines import KaplanMeierFitter
import matplotlib.pyplot as plt

def plot_survival_curve(durations: pd.Series, event_observed: pd.Series, title: str, output_path: str = None):
    """
    Plots a Kaplan-Meier survival curve with confidence intervals.
    """
    kmf = KaplanMeierFitter()
    kmf.fit(durations, event_observed=event_observed)
    ax = kmf.plot(ci_show=True)
    plt.title(title)
    plt.xlabel("Time")
    plt.ylabel("Survival Probability")
    plt.tight_layout()
    if output_path:
        plt.savefig(output_path)
    else:
        plt.show()
    plt.close()
