-- 607. Sales Person

SELECT name
FROM SalesPerson
WHERE sales_id NOT IN (
    SELECT s.sales_id
    FROM SalesPerson AS s
        JOIN Orders AS o ON s.sales_id = o.sales_id
        JOIN Company AS c ON o.com_id = c.com_id
    WHERE c.name = "RED"
);
