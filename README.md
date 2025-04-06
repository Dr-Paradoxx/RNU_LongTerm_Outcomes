# Long-term Oncological Outcomes in RNU/BCE for Upper Tract Urothelial Carcinoma

## Overview
This repository contains all materials related to our research project on long-term oncological outcomes following robot-assisted radical nephroureterectomy with bladder cuff excision (RNU/BCE) for the treatment of upper tract urothelial carcinoma (UTUC). The study investigates survival outcomes and factors affecting recurrence in patients treated at a single tertiary referral center. Our analysis encompasses recurrence-free survival (RFS), cancer-specific survival (CSS), and overall survival (OS) over follow-up periods extending up to 12 years.

## Background
UTUC is a challenging malignancy characterized by high recurrence and mortality rates. With the advent of robotic surgery, RNU/BCE has emerged as a minimally invasive alternative that aims to improve surgical outcomes while reducing patient morbidity. This project represents one of the longest-term single-center series evaluating the safety and efficacy of RNU/BCE, providing detailed survival analyses and insights into prognostic factors.

## Objectives
- **Primary Objective:**  
  Evaluate the long-term oncological outcomes (RFS, CSS, OS) following RNU/BCE in patients with UTUC.
- **Secondary Objectives:**  
  Identify factors associated with survival, including patient demographics, tumor characteristics, and perioperative variables.  
  Assess the impact of pathologic T stage and surgical margin status on cancer-specific survival.

## Methods
- **Study Design:**  
  Retrospective review of patients undergoing RNU/BCE at our institution from 2008 to 2022.
- **Data Collection:**  
  Patient demographics, perioperative data, pathological findings, and follow-up outcomes were systematically recorded.
- **Statistical Analysis:**  
  Survival outcomes were estimated using Kaplan-Meier analysis, while Cox proportional hazards regression models were employed to identify significant predictors of survival. Data analysis was performed using SAS (v9.4) and other statistical software.

## Key Results
- **Recurrence-Free Survival (RFS):**  
  1-year and 5-year RFS were reported as 67.1% and 37.8%, respectively.
- **Cancer-Specific Survival (CSS):**  
  1-year and 5-year CSS were 92.8% and 75.2%, respectively.
- **Overall Survival (OS):**  
  1-year and 5-year OS were 80.6% and 49.6%, with a median OS of 4.3 years.
- **Prognostic Factors:**  
  Multivariate analyses identified advanced age, positive surgical margins, pre-operative hydronephrosis, and certain comorbidities as significant factors adversely impacting survival outcomes.

## Repository Structure

RNU-project/
├── data/
│   ├── raw/                      
│   └── processed/                
├── manuscript/
│   ├── RNU.docx                
│   └── RNU_long_term_follow_up_manuscript.docx  
├── analysis/
│   ├── survival_analysis.py      
│   └── data_processing.py        
├── figures/                      
├── README.md                     
└── requirements.txt              

## How to Reproduce the Analysis
1. **Setup Environment:**  
   Install the required dependencies by running:
   ```bash
   pip install -r requirements.txt

2.	Data Preparation:
    Place all raw data files in the data/raw/ directory and run the data processing script:
    ```bash
     python analysis/data_processing.py

4.	Run Statistical Analyses:
    Execute the survival analysis script to generate survival curves and hazard ratios:
    ```bash
    python analysis/survival_analysis.py

4.	Review Figures:
    All generated figures will be saved in the figures/ folder for further review and inclusion in the manuscript.


# Contributions

Contributions to this project are welcome. If you would like to propose improvements or additional analyses, please submit a pull request or contact the corresponding author.


