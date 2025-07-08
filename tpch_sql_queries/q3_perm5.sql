
SELECT
    l_orderkey,
    SUM(l_extendedprice * (1 - l_discount)) AS revenue,
    o_orderdate,
    o_shippriority
FROM
    lineitem l, customer c, orders o
WHERE
    l_orderkey = o_orderkey
    AND c_custkey = o_custkey
    AND c_mktsegment = 'BUILDING'
    AND o_orderdate < DATE '1995-03-15'
    AND l_shipdate > DATE '1995-03-15'
GROUP BY
    l_orderkey, o_orderdate, o_shippriority
ORDER BY
    revenue DESC, o_orderdate
LIMIT 10;
