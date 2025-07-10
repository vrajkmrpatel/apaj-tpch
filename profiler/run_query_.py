import time
import psycopg2
import sys

# -------------------------------
# Usage: python run_query.py path_to_sql_query.sql
# -------------------------------

if len(sys.argv) != 2:
    print("Usage: python run_query.py path_to_sql_file.sql")
    sys.exit(1)

sql_file = sys.argv[1]

# Read SQL query from file
with open(sql_file, "r") as f:
    query = f.read()

# Connect to PostgreSQL
try:
    conn = psycopg2.connect(
        dbname="tpch",
        user="postgres",
        password="admin",   
        host="localhost",
        port="5432"
    )
    cur = conn.cursor()
except Exception as e:
    print("Error connecting to database:", e)
    sys.exit(1)

# Execute the query and time it
try:
    start = time.time()
    cur.execute(query)
    rows = cur.fetchall()
    duration = time.time() - start

    print(f"Execution Time: {duration:.4f} seconds")
    print(f"Rows Returned: {len(rows)}")
except Exception as e:
    print("Error executing query:", e)
finally:
    cur.close()
    conn.close()

# perf stat -e cache-misses python run_query_.py ../tpch_sql_queries/q5_perm1.sql