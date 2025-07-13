-- force join order
SET join_collapse_limit = 1;
SET from_collapse_limit = 1;

SELECT
    n.n_name,
    c.c_name,
    o.o_orderdate,
    SUM(l.l_extendedprice * (1 - l.l_discount)) AS total_revenue
FROM
    nation n
JOIN
    customer c ON n.n_nationkey = c.c_nationkey
JOIN
    orders o ON c.c_custkey = o.o_custkey
JOIN
    lineitem l ON o.o_orderkey = l.l_orderkey
WHERE
    o.o_orderdate BETWEEN DATE '1994-01-01' AND DATE '1994-12-31'
GROUP BY
    n.n_name, c.c_name, o.o_orderdate
ORDER BY
    total_revenue DESC;
