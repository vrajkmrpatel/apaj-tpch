import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the results
df_1 = pd.read_csv("results/perf_log_q5_1.csv")
df_50 = pd.read_csv("results/perf_log_q5_50.csv")
df_99 = pd.read_csv("results/perf_log_q5_99.csv")

# Add selectivity labels
df_1["Selectivity"] = "1%"
df_50["Selectivity"] = "50%"
df_99["Selectivity"] = "99%"

# Combine all into one
df_all = pd.concat([df_1, df_50, df_99])

# Set seaborn style
sns.set(style="whitegrid")

# Plot Histogram of Execution time
plt.figure(figsize=(10, 6))
sns.histplot(data=df_all, x="execution_time", hue="Selectivity", bins=10, kde=True, palette="Set2")
plt.title("Histogram of Execution time")
plt.xlabel("Execution time")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig("results/histogram_execution_time.png")
plt.show()
