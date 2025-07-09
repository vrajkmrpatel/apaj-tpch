import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load your performance log CSV file
df = pd.read_csv("perf_log.csv")  # Replace with actual path

# Sort permutations numerically
df["perm_index"] = df["query"].str.extract("(\d+)").astype(int)
df = df.sort_values("perm_index")

# Set position for each bar group
x = np.arange(len(df["query"]))  # label locations
width = 0.4  # width of the bars

# Create bar chart
fig, ax1 = plt.subplots(figsize=(14, 6))

bar1 = ax1.bar(x - width/2, df["time_secs"], width, label='Execution Time (s)', color='skyblue')
ax1.set_xlabel('Query Permutation')
ax1.set_ylabel('Execution Time (s)', color='skyblue')
ax1.tick_params(axis='y', labelcolor='skyblue')
ax1.set_xticks(x)
ax1.set_xticklabels(df["query"], rotation=45, ha='right')

# Create second y-axis for cache misses
ax2 = ax1.twinx()
bar2 = ax2.bar(x + width/2, df["cache_misses"], width, label='Cache Misses', color='salmon')
ax2.set_ylabel('Cache Misses', color='salmon')
ax2.tick_params(axis='y', labelcolor='salmon')

# Add title and legend
fig.suptitle('Execution Time and Cache Misses per Join Permutation')
fig.tight_layout()
fig.legend(loc='upper right', bbox_to_anchor=(1, 1), bbox_transform=ax1.transAxes)

# Save and show
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.savefig("perm_bargraph_time_vs_cache.png")
plt.show()
