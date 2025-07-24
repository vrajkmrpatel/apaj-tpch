import pandas as pd
import matplotlib.pyplot as plt
import argparse

def plot_exec_time(csv_file):
    # Read CSV
    df = pd.read_csv(csv_file)

    if 'permutation_id' not in df.columns or 'execution_time' not in df.columns:
        raise ValueError("CSV must contain 'permutation_id' and 'execution_time' columns")

    # Sort by permutation for consistent plotting
    df = df.sort_values("permutation_id")

    # Plot
    plt.figure(figsize=(10, 6))
    bars = plt.bar(df["permutation_id"], df["execution_time"], color='lightblue', edgecolor='black')

    # Add value labels
    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2, yval + 0.1, f"{yval:.2f}", ha='center', va='bottom')

    plt.title("Execution Time vs Permutations", fontsize=14)
    plt.xlabel("Permutation ID", fontsize=12)
    plt.ylabel("Execution Time (seconds)", fontsize=12)
    plt.xticks(rotation=45)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Plot execution time from CSV")
    parser.add_argument("csv_file", help="Path to CSV file with 'permutation_id' and 'execution_time' columns")
    args = parser.parse_args()

    plot_exec_time(args.csv_file)
