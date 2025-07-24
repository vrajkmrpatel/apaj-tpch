SELECT n_name, SUM(l_extendedprice * (1 - l_discount)) AS revenue
FROM orders
JOIN customer ON o_custkey = c_custkey
JOIN nation ON c_nationkey = n_nationkey
JOIN lineitem ON o_orderkey = l_orderkey
WHERE o_orderdate >= DATE '1994-01-01'
  AND o_orderdate < DATE '1995-01-01'
GROUP BY n_name
ORDER BY revenue DESC;
