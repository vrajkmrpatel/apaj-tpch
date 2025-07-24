SELECT n.n_name, SUM(l.l_extendedprice * (1 - l.l_discount)) AS revenue
FROM nation n
LEFT JOIN customer c ON c.c_nationkey = n.n_nationkey
LEFT JOIN orders o ON o.o_custkey = c.c_custkey 
                   AND o.o_orderdate >= DATE '1994-01-01'
                   AND o.o_orderdate < DATE '1995-01-01'
                   AND MOD(o.o_orderkey, 100) < 1
LEFT JOIN lineitem l ON l.l_orderkey = o.o_orderkey
GROUP BY n.n_name
ORDER BY revenue DESC;
