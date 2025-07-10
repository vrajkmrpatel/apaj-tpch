#!/usr/bin/env python3

import subprocess
import time
import csv
import os

SQL_DIR = "tpch_sql_queries"  # Update this to the actual directory path
DB_NAME = "tpch"         # Your PostgreSQL database name
OUTPUT_CSV = "results/perf_log.csv"
PERF_COUNTER = "cache-misses"  # You can add more if needed

os.makedirs("results", exist_ok=True)

with open(OUTPUT_CSV, "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["query", "time_secs", "cache_misses", "rows_returned", "first_join_pattern"])

    for i in range(1, 25):
        sql_file = f"{SQL_DIR}/q5_perm{i}.sql"
        cmd = [
            "perf", "stat", "-e", PERF_COUNTER, "--", "psql", "-d", DB_NAME, "-f", sql_file
        ]
        print(f"Running {sql_file}...")
        start = time.time()

        # Run command and capture output and perf stats
        proc = subprocess.run(cmd, capture_output=True, text=True)
        end = time.time()

        time_taken = round(end - start, 4)
        cache_miss = None
        rows_returned = None

        for line in proc.stderr.splitlines():
            if PERF_COUNTER in line:
                parts = line.strip().split()
                if parts:
                    try:
                        cache_miss = int(parts[0].replace(",", ""))
                    except:
                        cache_miss = -1

        for line in proc.stdout.splitlines():
            if "rows" in line.lower():
                try:
                    rows_returned = int(line.strip().split()[0])
                except:
                    rows_returned = -1

        writer.writerow([f"perm{i}", time_taken, cache_miss, rows_returned, ""])

print("Finished profiling all queries.")

# perf stat -e cache-references,cache-misses,L1-dcache-load-misses,l2_rqsts.miss,LLC-load-misses  python run_query_.py ../tpch_sql_queries/q5_perm1.sql