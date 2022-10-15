-- 608. Tree Node

SELECT
DISTINCT(t2.id) AS id,
CASE
    WHEN t2.p_id IS NULL THEN "Root"
    WHEN t1.p_id IS NULL THEN "Leaf"
    ELSE "Inner"
END AS type
FROM Tree AS t1
    RIGHT JOIN Tree AS t2 ON t1.p_id = t2.id
ORDER BY t2.id ASC;
