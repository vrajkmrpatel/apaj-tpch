import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Load the data
df_1 = pd.read_csv("results/perf_log_q5_1.csv")
df_50 = pd.read_csv("results/perf_log_q5_50.csv")
df_99 = pd.read_csv("results/perf_log_q5_99.csv")

# Add selectivity labels
df_1["Selectivity"] = "1%"
df_50["Selectivity"] = "50%"
df_99["Selectivity"] = "99%"

# Combine into one DataFrame
df_all = pd.concat([df_1, df_50, df_99])

# Set plotting style
sns.set(style="darkgrid", palette="pastel")

# Create subplots
fig, axes = plt.subplots(2, 1, figsize=(12, 10), sharex=True)

# Top plot: L1 Cache Misses per Tuple
sns.barplot(
    data=df_all,
    x="permutation_id",
    y="L1_misses_per_tuple",
    hue="Selectivity",
    ax=axes[0]
)
axes[0].set_title("L1 Cache Misses per Tuple across Join Permutations at Different Selectivities")
axes[0].set_ylabel("L1 Misses per Tuple")
axes[0].set_xlabel("")

# Bottom plot: Execution Time
sns.barplot(
    data=df_all,
    x="permutation_id",
    y="execution_time",
    hue="Selectivity",
    ax=axes[1]
)
axes[1].set_title("Execution Time across Join Permutations at Different Selectivities")
axes[1].set_ylabel("Execution Time (s)")
axes[1].set_xlabel("Join Permutation")

# Adjust layout
plt.tight_layout()
plt.savefig("results/q5_selectivity_analysis_combined.png")
plt.show()
