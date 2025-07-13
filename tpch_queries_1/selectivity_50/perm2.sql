-- force join order
SET join_collapse_limit = 1;
SET from_collapse_limit = 1;

SELECT
    n.n_name,
    c.c_name,
    o.o_orderdate,
    SUM(l.l_extendedprice * (1 - l.l_discount)) AS total_revenue
FROM
    customer c
JOIN
    orders o ON c.c_custkey = o.o_custkey
JOIN
    nation n ON c.c_nationkey = n.n_nationkey
JOIN
    lineitem l ON o.o_orderkey = l.l_orderkey
WHERE
    n.n_name IN ('UNITED STATES', 'CHINA', 'GERMANY', 'JAPAN', 'FRANCE')
    AND o.o_orderdate BETWEEN DATE '1994-01-01' AND DATE '1994-07-01'
    AND l.l_quantity BETWEEN 10 AND 20
GROUP BY
    n.n_name, c.c_name, o.o_orderdate
ORDER BY
    total_revenue DESC;
