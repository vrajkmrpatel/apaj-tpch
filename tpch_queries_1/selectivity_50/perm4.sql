-- force join order
SET join_collapse_limit = 1;
SET from_collapse_limit = 1;

SELECT
    n.n_name,
    c.c_name,
    o.o_orderdate,
    SUM(l.l_extendedprice * (1 - l.l_discount)) AS total_revenue
FROM
    orders o
JOIN
    customer c ON o.o_custkey = c.c_custkey
JOIN
    lineitem l ON o.o_orderkey = l.l_orderkey
JOIN
    nation n ON c.c_nationkey = n.n_nationkey
WHERE
    n.n_name IN ('UNITED STATES', 'CHINA', 'GERMANY', 'JAPAN', 'FRANCE')
    AND o.o_orderdate BETWEEN DATE '1994-01-01' AND DATE '1994-07-01'
    AND l.l_quantity BETWEEN 10 AND 20
GROUP BY
    n.n_name, c.c_name, o.o_orderdate
ORDER BY
    total_revenue DESC;
