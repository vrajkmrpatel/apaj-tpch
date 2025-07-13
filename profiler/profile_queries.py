#!/usr/bin/env python3

import subprocess
import time
import csv
import os

SQL_DIR = "tpch_queries_1"              # Directory where perm1.sql ... perm8.sql are
RUN_SCRIPT = "run_query_.py"            # Script that executes the SQL query
OUTPUT_CSV = "results_1/l1miss_log.csv" # Output CSV file
PERF_EVENT = "L1-dcache-load-misses"    # Event to capture

os.makedirs("results_1", exist_ok=True)

with open(OUTPUT_CSV, "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["query", "execution_time", "L1_cache_misses", "rows_returned"])

    for i in range(1, 9):  # perm1 to perm8
        sql_path = f"{SQL_DIR}/perm{i}.sql"
        cmd = [
            "perf", "stat", "-e", PERF_EVENT,
            "python3", RUN_SCRIPT, sql_path
        ]

        print(f"Running {sql_path} ...")
        start_time = time.time()
        proc = subprocess.run(cmd, capture_output=True, text=True)
        end_time = time.time()
        duration = round(end_time - start_time, 4)

        l1_misses = -1
        rows_returned = -1

        # Parse perf stderr output for L1 misses
        for line in proc.stderr.splitlines():
            if PERF_EVENT in line:
                try:
                    l1_misses = int(line.strip().split()[0].replace(',', ''))
                except:
                    l1_misses = -1

        # Parse stdout for returned rows
        for line in proc.stdout.splitlines():
            if "Rows Returned" in line:
                try:
                    rows_returned = int(line.strip().split(":")[-1].strip())
                except:
                    rows_returned = -1

        writer.writerow([f"perm{i}", duration, l1_misses, rows_returned])

print("✅ Finished profiling all queries.")
