# Software Requirements Specification (SRS)
## Project Title: HR Employee Attrition Data Cleaning and Exploratory Analysis

### 1. Introduction
This document describes the requirements, workflow, data cleaning steps, exploratory analysis logic, and outputs for the HR Employee Attrition Data Analysis project. The objective of this project is to take raw employee records from `HR-Employee-Attrition.csv`, clean and standardize the data in Python, save a clean working dataset, and analyze key factors associated with employee attrition.

### 2. Scope of the Project
The scope of this project covers:
- Loading raw HR employee data and checking its structure, rows, columns, and missing values.
- Cleaning duplicate records, text formatting issues, irrelevant constant columns, and invalid numeric values.
- Exporting a cleaned CSV dataset for downstream analysis.
- Performing exploratory data analysis across departments, overtime status, job roles, and monthly income.
- Generating visual charts to present the main observations clearly.
- Maintaining project documentation in the repository (`AVIRAL_AGARWAL_2026B01010619`).

### 3. System and Software Requirements
#### 3.1 Software & Libraries Used
- **Programming Language:** Python
- **Data Analysis Library:** `pandas` for reading CSV files, filtering rows/columns, grouping data, and calculating summary statistics
- **Visualization Library:** `matplotlib` for creating and saving bar charts as PNG files
- **Code Editor:** Visual Studio Code (VS Code)
- **Version Control & Hosting:** Git and GitHub

#### 3.2 Hardware & OS Environment
- Standard desktop/laptop system capable of running Python scripts and storing CSV and PNG files locally.
- Tested in Windows PowerShell environment with a local project directory and Git remote connected to GitHub.

### 4. Dataset Overview and File Structure
#### 4.1 Dataset Details
- **Input File:** `HR-Employee-Attrition.csv` containing `1,470` rows (employee records) and `35` columns initially.
- **Cleaned Output File:** `data/cleaned_hr_attrition.csv` containing `1,470` rows and `33` columns after dropping the zero-variance constant columns and adding the `Attrition_Flag` column.

#### 4.2 Repository Structure
- `HR-Employee-Attrition.csv` — Raw input dataset containing employee demographic, job, compensation, and attrition fields.
- `clean_data.py` — Python script that performs data loading, deduplication, whitespace trimming, constant column removal, target standardization, numeric validation, and CSV export.
- `data/cleaned_hr_attrition.csv` — Cleaned dataset generated after running `clean_data.py`.
- `eda_and_analysis.py` — Python script that reads the cleaned dataset, prints group-wise summaries, checks job role attrition rates, and saves charts into `charts/`.
- `charts/` — Folder storing generated PNG plots (`attrition_by_department.png`, `attrition_by_overtime.png`, and `income_by_attrition.png`).
- `README.md` — Project summary, folder overview, key findings, and run commands.
- `SRS.md` — Detailed project specification covering requirements, processing steps, outputs, findings, and limitations.

### 5. Functional Requirements and Processing Steps
#### 5.1 Data Loading and Inspection
- The program reads `HR-Employee-Attrition.csv` using `pandas.read_csv()` with `utf-8-sig` encoding so special characters or BOM markers do not cause column name issues.
- The script prints initial row and column counts and checks for missing values across columns.

#### 5.2 Data Cleaning Rules (`clean_data.py`)
- **Duplicate Removal:** Exact duplicate rows are removed, and if `EmployeeNumber` is present, duplicate employee records are filtered while keeping the first entry.
- **String Normalization:** Leading and trailing spaces are removed from text/object columns so category labels stay consistent.
- **Constant Column Removal:** Columns that have only one unique value across the dataset (`EmployeeCount`, `Over18`, and `StandardHours`) are dropped because they do not add variation for comparison.
- **Target Field Standardization:** `Attrition` values are normalized (`Yes` / `No`) and mapped into a numeric `Attrition_Flag` column (`1` for `Yes` and `0` for `No`) to make rate and average calculations straightforward.
- **Numeric Range Checks:** Basic checks keep `Age` between `18` and `70` and `MonthlyIncome` greater than `0`.
- **Output Generation:** The cleaned table is written to `data/cleaned_hr_attrition.csv` without row index numbers.

#### 5.3 Exploratory Data Analysis and Chart Generation (`eda_and_analysis.py`)
- Loads `data/cleaned_hr_attrition.csv` and creates the `charts/` directory if it does not already exist.
- Calculates the overall attrition rate percentage across the dataset.
- Groups data by `Department` to compute attrition rates and saves `charts/attrition_by_department.png`.
- Groups data by `OverTime` (`Yes` vs. `No`) to compare attrition rates and saves `charts/attrition_by_overtime.png`.
- Groups data by `Attrition` (`Yes` vs. `No`) to compare average `MonthlyIncome` and saves `charts/income_by_attrition.png`.
- Computes and prints attrition rate percentages across `JobRole` categories.

### 6. Observed Findings from Analysis
- **Department Comparison:** Sales has the highest attrition rate at `20.63%`, followed by Human Resources at `19.05%`, while Research & Development has the lowest attrition rate at `13.84%`.
- **Overtime Comparison:** Employees who work overtime (`Yes`) show a `30.53%` attrition rate compared to `10.44%` among employees who do not work overtime (`No`).
- **Monthly Income Comparison:** Employees who left (`Attrition = Yes`) have a lower average monthly income (`4,787.09`) than employees who stayed (`6,832.74`).

### 7. Non-Functional Requirements
- **Maintainability:** Code is separated into modular scripts (`clean_data.py` and `eda_and_analysis.py`) using `pathlib.Path` so paths resolve cleanly across runs.
- **Reproducibility:** Running the scripts in order reproduces the same cleaned CSV file, console summaries, and PNG chart outputs.
- **Readability:** Clear variable names, console section headers, and structured markdown documentation make the project easy to follow and review.

### 8. How to Run the Project
Execute the scripts from the project root directory in terminal:
```bash
python clean_data.py
python eda_and_analysis.py