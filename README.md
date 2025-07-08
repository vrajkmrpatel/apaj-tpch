
# Access Pattern-Aware Joins on TPC-H

This project implements an **Access Pattern-Aware Join (APAJ)** optimization strategy using TPC-H benchmark queries. It analyzes how different join orders affect performance through memory access patterns, and uses a lightweight **ML classifier** trained on hardware performance counters (like cache misses) to guide adaptive join reordering.

---

## 🧠 Core Idea

Different join orders induce different memory access patterns (`Sequential`, `Random`, `Pseudo-Random`). These patterns significantly affect CPU cache behavior and execution time.

APAJ learns these patterns at runtime using **perf counters** and reorders joins to minimize random memory access early in the pipeline — leading to lower cache misses and faster execution.

---

## 🔬 Features

- ✅ Run all permutations of a given join query (e.g., TPC-H Q3)
- ✅ Measure execution time and cache behavior using `perf`
- ✅ Train a neural network to classify join access patterns
- ✅ Predict pattern of a new query and reorder joins adaptively
- ✅ Full support for PostgreSQL & TPC-H datasets

---

## 📁 Folder Structure

```
.
├── tpch_sql_queries/        # 6 permutations of TPC-H Q3
├── results/            # perf_log.csv with profiling results
├── profiler/           # run_query.py script using perf
├── ml_model/           # train_classifier.py for access pattern classification
└── README.md
```

---

## 🚀 How to Run

### 1. Generate or load your TPC-H dataset
Use DuckDB or PostgreSQL with DBGEN to load TPC-H tables.

### 2. Run query permutations
```bash
python profiler/run_query.py
```

### 3. Measure each permutation's cache-misses
```bash
perf stat -e cache-misses psql -f q3_perm1.sql
```

### 4. Update and label `results/perf_log.csv`

### 5. Train ML model
```bash
python ml_model/train_classifier.py
```

---

## 🛠 Tools Used

- Python 3.10
- PostgreSQL (or DuckDB)
- `perf` for profiling
- `scikit-learn`, `joblib` for ML
- TPC-H benchmark data

---

## 📈 Sample Output

```csv
query,time_secs,cache_misses,rows_returned,first_join_pattern
perm1,0.47,1136574,10,Random
perm2,0.41,1007977,10,Pseudo-Random
perm3,0.40,920503,10,Sequential
```

---

## 📚 References

- [📄 Original Paper PDF](resource/apaj.pdf)

- Schubert et al., *"Exploiting Access Pattern Characteristics for Join Reordering"*, SIGMOD 2022
- TPC-H Benchmark: https://www.tpc.org/tpch/
- `perf`: Linux Performance Counters

---
