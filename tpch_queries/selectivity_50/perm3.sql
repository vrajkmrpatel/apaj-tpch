SELECT
    n_name,
    SUM(l_extendedprice * (1 - l_discount)) AS revenue
FROM
    customer
    JOIN nation ON customer.c_nationkey = nation.n_nationkey 
    JOIN orders ON customer.c_custkey = orders.o_custkey 
    JOIN lineitem ON orders.o_orderkey = lineitem.l_orderkey
WHERE
    o_orderdate BETWEEN DATE '1994-01-01' AND DATE '1994-06-01'
    AND l_shipdate BETWEEN DATE '1994-02-01' AND DATE '1994-08-01'
    AND customer.c_mktsegment IN ('AUTOMOBILE', 'HOUSEHOLD')
GROUP BY
    n_name
ORDER BY
    revenue DESC;
