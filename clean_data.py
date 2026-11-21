from pathlib import Path
import pandas as pd


def clean_hr_data(input_path: Path, output_path: Path) -> pd.DataFrame:
    # Load CSV (encoding="utf-8-sig" handles UTF-8 with BOM cleanly)
    df = pd.read_csv(input_path, encoding="utf-8-sig")

    print(f"Initial shape: {df.shape[0]} rows, {df.shape[1]} columns")
    print("Missing values per column:\n", df.isna().sum()[df.isna().sum() > 0])

    # 1. Remove exact duplicate rows and duplicate employee IDs (keep first occurrence)
    df = df.drop_duplicates().copy()
    if "EmployeeNumber" in df.columns:
        df = df.drop_duplicates(subset=["EmployeeNumber"], keep="first").copy()

    # 2. Strip whitespace from string/object columns
    object_cols = df.select_dtypes(include=["object", "string"]).columns
    for col in object_cols:
        df[col] = df[col].astype(str).str.strip()

    # 3. Drop constant columns (only 1 unique value) that add no analytical signal
    constant_cols = [col for col in df.columns if df[col].nunique(dropna=False) <= 1]
    if constant_cols:
        print("Dropping constant columns:", constant_cols)
        df = df.drop(columns=constant_cols)

    # 4. Standardize target column and create a numeric attrition indicator
    if "Attrition" in df.columns:
        df["Attrition"] = df["Attrition"].str.title()  # "Yes" / "No"
        df["Attrition_Flag"] = df["Attrition"].map({"Yes": 1, "No": 0})

    # 5. Basic sanity checks on key numeric fields
    if "Age" in df.columns:
        df = df[(df["Age"] >= 18) & (df["Age"] <= 70)].copy()
    if "MonthlyIncome" in df.columns:
        df = df[df["MonthlyIncome"] > 0].copy()

    # Save cleaned dataset
    output_path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(output_path, index=False)
    print(f"Cleaned shape: {df.shape[0]} rows, {df.shape[1]} columns")
    print(f"Saved cleaned data to: {output_path}")

    return df


if __name__ == "__main__":
    base_dir = Path(__file__).resolve().parent
    # Adjust raw_file if HR-Employee-Attrition.csv is in base_dir / "data" / "HR-Employee-Attrition.csv"
    raw_file = base_dir / "HR-Employee-Attrition.csv"
    cleaned_file = base_dir / "data" / "cleaned_hr_attrition.csv"

    clean_hr_data(raw_file, cleaned_file)