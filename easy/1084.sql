-- 1084. Sales Analysis III

SELECT Sales.product_id AS product_id, Product.product_name AS product_name
FROM Sales
    JOIN Product ON Sales.product_id = Product.product_id
GROUP BY product_id
HAVING MIN(sale_date) >= "2019-01-01" AND MAX(sale_date) <= "2019-03-31";
