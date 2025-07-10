SELECT
    n_name,
    SUM(l_extendedprice * (1 - l_discount)) AS revenue
FROM
    orders
    JOIN customer ON customer.c_custkey = orders.o_custkey 
    JOIN nation ON customer.c_nationkey = nation.n_nationkey 
    JOIN lineitem ON orders.o_orderkey = lineitem.l_orderkey
WHERE
    o_orderdate BETWEEN DATE '1994-01-01' AND DATE '1994-01-03'
    AND l_shipdate BETWEEN DATE '1994-02-01' AND DATE '1994-02-03'
    AND customer.c_mktsegment = 'AUTOMOBILE'
GROUP BY
    n_name
ORDER BY
    revenue DESC;