import pandas as pd
import matplotlib.pyplot as plt

# Load your performance log CSV file
df = pd.read_csv("perf_log.csv")  # Replace with the correct path if needed

# Sort by permutation name (assuming it's named like 'perm1', 'perm2', ...)
df["perm_index"] = df["query"].str.extract('(\d+)').astype(int)
df.sort_values("perm_index", inplace=True)

# Plotting execution time and cache misses
fig, ax1 = plt.subplots(figsize=(12, 6))

# Plot execution time on left Y-axis
color = 'tab:blue'
ax1.set_xlabel('Permutation')
ax1.set_ylabel('Execution Time (seconds)', color=color)
ax1.plot(df["query"], df["time_secs"], color=color, marker='o', label="Execution Time")
ax1.tick_params(axis='y', labelcolor=color)
ax1.set_xticklabels(df["query"], rotation=45, ha='right')

# Plot cache misses on right Y-axis
ax2 = ax1.twinx()
color = 'tab:red'
ax2.set_ylabel('Cache Misses', color=color)
ax2.plot(df["query"], df["cache_misses"], color=color, marker='s', label="Cache Misses")
ax2.tick_params(axis='y', labelcolor=color)

# Add title and grid
plt.title("Execution Time and Cache Misses Across Permutations")
fig.tight_layout()
plt.grid(True, axis='y', linestyle='--', alpha=0.5)

# Save the plot
plt.savefig("perm_vs_time_and_cache.png")
plt.show()
