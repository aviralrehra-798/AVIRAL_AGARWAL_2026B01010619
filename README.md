# HR Employee Attrition Data Analysis

## Project Overview
This project cleans and analyzes employee attrition data (`1,470` employee records) to identify the primary drivers behind employee turnover.

## Project Structure
- `HR-Employee-Attrition.csv`: Raw dataset
- `clean_data.py`: Cleans raw data, removes constant columns (`EmployeeCount`, `Over18`, `StandardHours`), strips whitespace, and creates `Attrition_Flag`
- `data/cleaned_hr_attrition.csv`: Cleaned dataset ready for analysis
- `eda_and_analysis.py`: Computes attrition breakdowns and generates visual charts
- `charts/`: Exported PNG visualizations

## Key Findings
- **Department Impact:** Sales has the highest attrition rate (`20.63%`), followed by Human Resources (`19.05%`) and Research & Development (`13.84%`).
- **OverTime Impact:** Employees working overtime leave at nearly **3x the rate** (`30.53%`) compared to those without overtime (`10.44%`).
- **Compensation Gap:** Employees who left earned a noticeably lower average monthly income (`4,787.09`) than those who stayed (`6,832.74`).

## How to Run
```bash
python clean_data.py
python eda_and_analysis.py
