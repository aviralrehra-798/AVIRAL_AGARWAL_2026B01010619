from pathlib import Path
import matplotlib.pyplot as plt
import pandas as pd


def run_eda_and_charts(cleaned_path: Path, charts_dir: Path) -> None:
    df = pd.read_csv(cleaned_path)
    charts_dir.mkdir(parents=True, exist_ok=True)

    # 1. Overall Attrition
    overall_rate = round(df["Attrition_Flag"].mean() * 100, 2)
    print(f"Overall Attrition Rate: {overall_rate}%")

    # 2. Attrition by Department (Chart 1)
    dept_rate = (df.groupby("Department")["Attrition_Flag"].mean() * 100).round(2).sort_values(ascending=False)
    print("\n=== Attrition Rate (%) by Department ===")
    print(dept_rate)

    plt.figure(figsize=(8, 5))
    dept_rate.plot(kind="bar", color=["#e74c3c", "#f39c12", "#3498db"])
    plt.title("Attrition Rate (%) by Department")
    plt.ylabel("Attrition Rate (%)")
    plt.xticks(rotation=0)
    plt.tight_layout()
    plt.savefig(charts_dir / "attrition_by_department.png", dpi=150)
    plt.close()

    # 3. Attrition by OverTime (Chart 2)
    ot_rate = (df.groupby("OverTime")["Attrition_Flag"].mean() * 100).round(2).sort_values(ascending=False)
    print("\n=== Attrition Rate (%) by OverTime ===")
    print(ot_rate)

    plt.figure(figsize=(6, 5))
    ot_rate.plot(kind="bar", color=["#e74c3c", "#2ecc71"])
    plt.title("Attrition Rate (%) by OverTime")
    plt.ylabel("Attrition Rate (%)")
    plt.xticks(rotation=0)
    plt.tight_layout()
    plt.savefig(charts_dir / "attrition_by_overtime.png", dpi=150)
    plt.close()

    # 4. Average MonthlyIncome by Attrition (Chart 3)
    income_avg = df.groupby("Attrition")["MonthlyIncome"].mean().round(2)
    print("\n=== Average MonthlyIncome by Attrition ===")
    print(income_avg)

    plt.figure(figsize=(6, 5))
    income_avg.plot(kind="bar", color=["#2ecc71", "#e74c3c"])
    plt.title("Average Monthly Income: Stayed (No) vs Left (Yes)")
    plt.ylabel("Average Monthly Income")
    plt.xticks(rotation=0)
    plt.tight_layout()
    plt.savefig(charts_dir / "income_by_attrition.png", dpi=150)
    plt.close()

    # 5. Top JobRoles by Attrition Rate
    role_rate = (df.groupby("JobRole")["Attrition_Flag"].mean() * 100).round(2).sort_values(ascending=False)
    print("\n=== Attrition Rate (%) by JobRole ===")
    print(role_rate)

    print(f"\nAll 3 charts saved inside: {charts_dir}")


if __name__ == "__main__":
    base_dir = Path(__file__).resolve().parent
    cleaned_file = base_dir / "data" / "cleaned_hr_attrition.csv"
    output_charts = base_dir / "charts"

    run_eda_and_charts(cleaned_file, output_charts)