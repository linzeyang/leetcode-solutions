-- 100177. Binary Tree Nodes

SELECT DISTINCT
    (t1.N) AS N,
    CASE
        WHEN t1.P IS NULL THEN "Root"
        WHEN t2.N IS NULL THEN "Leaf"
        ELSE "Inner"
    END AS `Type`
FROM
    Tree AS t1
    LEFT JOIN Tree AS t2 ON t1.N = t2.P
ORDER BY
    N;
