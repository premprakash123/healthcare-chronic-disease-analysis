# 🏥 Healthcare Chronic Disease Prediction & EHR Analysis

## 📌 Project Overview

This project focuses on analyzing anonymized Electronic Health Records (EHR) data to predict Chronic Kidney Disease (CKD) using Machine Learning techniques.

The project includes:

- 🧹 Data Cleaning & Preprocessing
- 📊 Exploratory Data Analysis (EDA)
- 🤖 Machine Learning Modeling
- 📈 Healthcare Dashboard Development
- 📑 Professional Documentation

---

# 🎯 Objectives

✅ Identify high-risk patients  
✅ Analyze important medical biomarkers  
✅ Build predictive healthcare models  
✅ Generate actionable healthcare insights  

---

# 🛠️ Tech Stack

| Category | Tools |
|---|---|
| Programming | Python |
| Data Analysis | Pandas, NumPy |
| Visualization | Matplotlib, Seaborn |
| Machine Learning | Scikit-Learn |
| Dashboard | Power BI / Tableau |
| Version Control | Git & GitHub |

---

# 📂 Project Structure

```text
healthcare-chronic-disease-analysis/
│
├── data/
├── notebooks/
├── scripts/
├── models/
├── visuals/
├── reports/
├── dashboard/
├── README.md
└── .gitignore
```

---

# 📊 Dataset

Dataset: Chronic Kidney Disease (CKD) Dataset  
Source: UCI Machine Learning Repository

---

# 🚀 Project Status

📅 Week 1 — 
# 📅 Day 1 — Environment Setup & Project Initialization

## 🎯 Objective

The objective of Day 1 was to establish the foundational infrastructure for the Healthcare Chronic Disease Prediction project using enterprise-grade development and version control practices.

This phase focused on preparing the development environment, organizing the project architecture, and initializing a professional GitHub workflow.

---

# 🛠️ Tasks Completed

✅ Created project repository  
✅ Initialized Git version control  
✅ Configured project folder architecture  
✅ Setup Anaconda environment  
✅ Installed required Python libraries  
✅ Configured VS Code + Jupyter workflow  
✅ Created notebook and script structure  
✅ Added professional `.gitignore`  
✅ Created initial README documentation  

---

# 🧱 Project Structure Initialization

The following professional directory structure was created:

```text
healthcare-chronic-disease-analysis/
│
├── data/
│   ├── raw/
│   ├── processed/
│   └── external/
│
├── notebooks/
├── scripts/
├── models/
├── visuals/
├── reports/
├── dashboard/
│
├── README.md
├── requirements.txt
└── .gitignore
```

---

# ⚙️ Environment Configuration

## Anaconda Environment

A dedicated Conda environment was created for isolated dependency management.

```bash
conda create -n healthcare-analytics python=3.11
```

Environment activation:

```bash
conda activate healthcare-analytics
```

---

# 📦 Libraries Installed

The following libraries were installed for healthcare analytics and machine learning workflows:

```text
pandas
numpy
matplotlib
seaborn
scikit-learn
scipy
imbalanced-learn
jupyter
```

---

# 💻 Development Workflow

The development workflow was configured using:

- VS Code
- Jupyter Notebook
- Git Bash
- GitHub

This setup enables:

✅ Reproducible analysis  
✅ Professional Git version control  
✅ Notebook-based experimentation  
✅ Structured project management  

---

# 🔐 Git & GitHub Configuration

## Repository Initialization

Git version control was initialized locally and connected to GitHub for continuous contribution tracking.

## Branching Workflow

A professional branching strategy was planned to separate:

- Data cleaning
- EDA
- Modeling
- Dashboard development

---

# 🧹 .gitignore Configuration

A professional `.gitignore` file was added to exclude:

- Raw datasets
- Temporary notebook files
- Environment variables
- Cache files
- Large binary outputs

This ensures a clean and secure repository structure.

---

# 📑 Initial Documentation

An initial `README.md` file was created containing:

- Project overview
- Objectives
- Technology stack
- Folder structure
- Dataset information

---

# 📌 Professional Practices Followed

The following enterprise-grade practices were established from Day 1:

✅ Semantic Git commit messages  
✅ Modular project structure  
✅ Daily contribution workflow  
✅ Secure dataset handling  
✅ Environment isolation using Conda  
✅ Documentation-first approach  

---
# 📅 Day 2 — Dataset Collection & Understanding

## 🎯 Objective

The objective of Day 2 was to collect, inspect, and understand the Chronic Kidney Disease (CKD) dataset before beginning preprocessing and analysis.

---

# 📂 Dataset Acquisition

## Dataset Used
Chronic Kidney Disease Dataset

## Source
UCI Machine Learning Repository

## Original Format
`.arff`

The dataset was initially provided in ARFF format and later converted into CSV format for easier preprocessing, analysis, and dashboard integration.

---

# 🛠️ Tasks Completed

✅ Downloaded CKD dataset  
✅ Read dataset documentation  
✅ Loaded dataset into Jupyter Notebook  
✅ Converted ARFF file into Pandas DataFrame  
✅ Decoded categorical byte values  
✅ Exported processed CSV dataset  
✅ Performed initial inspection and validation  

---

# 📊 Initial Dataset Inspection

The following checks were performed:

- Dataset shape
- Column names
- Data types
- Missing values
- Target variable distribution
- Unique categorical values

---

# 🔍 Key Observations

- Several medical attributes contain missing values
- Some categorical columns were encoded as byte strings
- A few columns required datatype correction
- Dataset contains both numerical and categorical healthcare variables

---

# 🧹 Initial Processing Performed

## ARFF Conversion
The dataset was converted from ARFF format into a Pandas DataFrame using Scipy.

## Byte Decoding
Categorical byte values were decoded into readable string format.

## CSV Export
A clean intermediate CSV file was exported for downstream preprocessing.

---

# 📁 Output Files Generated

```text
data/raw/chronic_kidney_disease.arff
data/processed/ckd_clean_initial.csv
```
---
# 📅 Day 3 — Missing Value Handling & Data Preprocessing

## 🎯 Objective

The objective of Day 3 was to clean the healthcare dataset by handling missing values, correcting invalid entries, standardizing data types, and preparing the dataset for exploratory analysis and machine learning.

---

# 🛠️ Tasks Completed

✅ Identified missing value patterns  
✅ Removed unwanted columns  
✅ Replaced invalid symbols with null values  
✅ Corrected inconsistent data types  
✅ Applied median imputation for numerical features  
✅ Applied mode imputation for categorical features  
✅ Validated cleaned dataset integrity  
✅ Exported finalized cleaned dataset  

---

# 🔍 Missing Value Assessment

A detailed missing value analysis was performed using:

- `df.isnull().sum()`
- Missing value heatmaps
- Column-wise inspection

Several healthcare biomarker columns contained missing observations, including:

- Red Blood Cell Count
- White Blood Cell Count
- Sodium
- Potassium
- Hemoglobin

---

# ⚠️ Invalid Data Handling

The dataset contained invalid placeholders such as:

```text
?
\\t?
blank spaces
```

These values were replaced with proper `NaN` entries to ensure accurate preprocessing.

---

# 🔄 Data Type Correction

Several numerical medical attributes were incorrectly stored as object/string types.

The following preprocessing steps were performed:

- Removed hidden spaces
- Converted columns using `pd.to_numeric()`
- Coerced invalid entries into missing values

---

# 📊 Numerical Imputation Strategy

## Median Imputation

Median imputation was applied to numerical healthcare attributes.

### Why Median?

Healthcare biomarker data often contains:

- Outliers
- Skewed distributions
- Extreme medical values

Median is more robust than mean and prevents distortion of clinical measurements.

---

# 🧩 Categorical Imputation Strategy

## Mode Imputation

Mode imputation was used for categorical medical variables because it preserves the most frequently observed category while maintaining dataset consistency.

---

# 🧹 Additional Cleaning

The following additional preprocessing tasks were completed:

- Duplicate record inspection
- Removal of unnecessary unnamed columns
- Dataset validation after imputation

---

# 📁 Output Files Generated

```text
data/processed/ckd_cleaned.csv
```

---

# 📌 Final Validation

The cleaned dataset was validated to ensure:

✅ No critical missing values remain  
✅ Correct data types are assigned  
✅ Dataset is ready for EDA and ML workflows  

---

# 💻 Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn

---

# 📅 Day 4 — Exploratory Data Analysis (EDA)

## 🎯 Objective

The objective of Day 4 was to perform Exploratory Data Analysis (EDA) on the cleaned Chronic Kidney Disease (CKD) dataset in order to identify important healthcare patterns, biomarker relationships, feature distributions, and potential risk indicators before machine learning preparation.

---

# 🛠️ Tasks Completed

✅ Loaded cleaned healthcare dataset  
✅ Performed statistical dataset overview  
✅ Analyzed CKD target variable distribution  
✅ Visualized numerical feature distributions  
✅ Conducted outlier inspection using boxplots  
✅ Generated healthcare biomarker correlation heatmap  
✅ Compared healthy vs diseased patient groups  
✅ Documented key healthcare insights  

---

# 📂 Dataset Used

```text
data/processed/ckd_cleaned.csv
```

The cleaned dataset generated during Day 3 preprocessing was used for exploratory analysis.

---

# 📊 Dataset Overview

The following inspections were performed:

- Dataset shape analysis
- Data type verification
- Descriptive statistics
- Numerical feature summaries
- Categorical feature assessment

---

# 🧠 Target Variable Analysis

The CKD target variable distribution was analyzed to understand the balance between:

- CKD Positive Patients
- CKD Negative Patients

A countplot visualization was generated to inspect disease prevalence within the dataset.

---

# 📈 Feature Distribution Analysis

Histogram visualizations were created to analyze the distribution of healthcare biomarkers such as:

- Blood Pressure
- Hemoglobin
- Serum Creatinine
- Blood Glucose
- Sodium
- Potassium

This analysis helped identify:

✅ Skewed distributions  
✅ Feature spread  
✅ Abnormal clinical ranges  
✅ Potential outliers  

---

# 📦 Outlier Inspection

Boxplots were generated for numerical healthcare features to inspect the presence of extreme biomarker values.

### Key Observation

Healthcare datasets naturally contain abnormal biomarker measurements due to clinical conditions. Outlier inspection was performed to understand data variability before machine learning modeling.

---

# 🔥 Correlation Analysis

A healthcare biomarker correlation heatmap was generated to identify relationships between medical variables.

## Important Note

A temporary encoded copy of the dataset was created because correlation matrices require numerical feature representations.

The original healthcare dataset remained unchanged during this process.

---

# 🔍 Disease vs Healthy Patient Analysis

Comparative visualizations were created between:

- CKD Positive Patients
- Healthy Patients

This helped identify biomarkers strongly associated with chronic kidney disease risk.

Example analyses included:

- Hemoglobin distribution
- Serum creatinine comparison
- Blood pressure variation

---

# 📌 Key EDA Findings

### Observed Insights

- CKD patients generally showed abnormal biomarker distributions
- Serum creatinine exhibited strong disease association
- Hemoglobin levels were comparatively lower in CKD-positive patients
- Several healthcare features displayed visible correlations
- Outliers were present across multiple medical attributes

---

# 📊 Visualizations Generated

The following visualizations were created:

✅ Histograms  
✅ Countplots  
✅ Boxplots  
✅ Correlation Heatmaps  
✅ Disease Comparison Plots  
✅ Distribution Analysis Charts  

---

# 💻 Technologies Used

- Python
- Pandas
- Matplotlib
- Seaborn

---

# 🚀 Next Steps

The next phase will focus on:

- Label Encoding
- Feature Standardization
- Feature Engineering
- SMOTE for class balancing
- ML-ready dataset preparation

---

# 🔐 Professional Notes

- EDA was performed on a cleaned and validated healthcare dataset
- Original medical data integrity was preserved
- Temporary encoding was used only for correlation analysis
- Visual analysis was documented for reproducibility
- Professional notebook structure and semantic Git commits were maintained throughout the workflow