-- 1327. List the Products Ordered in a Period

SELECT P.product_name, SUM(unit) AS unit
FROM Products AS P
    JOIN Orders AS O ON P.product_id = O.product_id
WHERE order_date BETWEEN "2020-02-01" AND "2020-02-29"
GROUP BY O.product_id
HAVING SUM(unit) > 99;
