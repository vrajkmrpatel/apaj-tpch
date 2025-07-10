SELECT
    n_name,
    SUM(l_extendedprice * (1 - l_discount)) AS revenue
FROM
    orders
    JOIN lineitem ON orders.o_orderkey = lineitem.l_orderkey 
    JOIN customer ON customer.c_custkey = orders.o_custkey 
    JOIN nation ON customer.c_nationkey = nation.n_nationkey
WHERE
    o_orderdate BETWEEN DATE '1994-01-01' AND DATE '1994-06-01'
    AND l_shipdate BETWEEN DATE '1994-02-01' AND DATE '1994-08-01'
    AND customer.c_mktsegment IN ('AUTOMOBILE', 'HOUSEHOLD')
GROUP BY
    n_name
ORDER BY
    revenue DESC;