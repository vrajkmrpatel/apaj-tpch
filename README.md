
# Mini APAJ Experiment (Access Pattern-Aware Join Reordering)

This project replicates a small-scale version of the APAJ (Access Pattern-Aware Join) experiment using PostgreSQL, Linux `perf`, and a simple ML model.

## Structure

- `sql_queries/`: Contains 6 permutations of 3-way join SQL queries (A, B, C)
- `data_generator/`: Python script to create synthetic data for tables A, B, and C
- `profiler/`: Python script to run queries and measure execution time + cache misses via `perf`
- `ml_model/`: Code to train a simple classifier to predict access pattern based on cache stats
- `adaptive_join_selector/`: Implements Algorithm 1 to select better join order adaptively
- `results/`: CSV files with measurements, access patterns, predictions, and performance

## Requirements

- PostgreSQL
- Python 3.10+
- `psycopg2`, `scikit-learn`, `pandas`, `matplotlib`
- Linux `perf` tool
