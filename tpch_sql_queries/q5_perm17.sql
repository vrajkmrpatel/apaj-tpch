SELECT
    n_name,
    SUM(l_extendedprice * (1 - l_discount)) AS revenue
FROM
    lineitem,
    nation,
    customer,
    orders
WHERE
    c_custkey = o_custkey
    AND o_orderkey = l_orderkey
    AND c_nationkey = n_nationkey
    AND o_orderdate >= DATE '1994-01-01'
    AND o_orderdate < DATE '1995-01-01'
GROUP BY
    n_name
ORDER BY
    revenue DESC;