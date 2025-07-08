
import psycopg2
import random

conn = psycopg2.connect(dbname="postgres", user="postgres", password="admin", host="localhost")
cur = conn.cursor()

# Drop if exists
cur.execute("DROP TABLE IF EXISTS A, B, C;")

# Create tables
cur.execute("CREATE TABLE A(id INT PRIMARY KEY, val INT);")
cur.execute("CREATE TABLE B(id INT PRIMARY KEY, a_id INT, val INT);")
cur.execute("CREATE TABLE C(id INT PRIMARY KEY, a_id INT, val INT);")

# Insert data
for i in range(1, 100001):
    cur.execute("INSERT INTO A VALUES (%s, %s);", (i, random.randint(1, 1000)))
    cur.execute("INSERT INTO B VALUES (%s, %s, %s);", (i, random.randint(1, 100000), random.randint(1, 1000)))
    cur.execute("INSERT INTO C VALUES (%s, %s, %s);", (i, random.randint(1, 100000), random.randint(1, 1000)))

conn.commit()
cur.close()
conn.close()
print("Tables A, B, C populated.")
