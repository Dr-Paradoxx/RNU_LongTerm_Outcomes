from setuptools import setup, find_packages

setup(
    name="RNU_LongTerm_Outcomes",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "pandas",
        "numpy",
        "matplotlib",
        "scipy",
        "openpyxl",
        "scikit-learn",
        "lifelines"
    ],
    entry_points={
        "console_scripts": [
            "rnu_analysis=main:main",
        ],
    },
)
