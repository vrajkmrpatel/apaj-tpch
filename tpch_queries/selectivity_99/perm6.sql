SELECT
    n_name,
    SUM(l_extendedprice * (1 - l_discount)) AS revenue
FROM
    orders
    JOIN lineitem ON orders.o_orderkey = lineitem.l_orderkey 
    JOIN customer ON customer.c_custkey = orders.o_custkey 
    JOIN nation ON customer.c_nationkey = nation.n_nationkey
WHERE
    o_orderdate >= DATE '1994-01-01'
    AND o_orderdate < DATE '1995-01-01'
GROUP BY
    n_name
ORDER BY
    revenue DESC;