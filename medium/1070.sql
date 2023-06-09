-- 1070. Product Sales Analysis III

SELECT S.product_id, TEMP.first_year, quantity, price
FROM Sales AS S
    JOIN (
        SELECT product_id, MIN(year) AS first_year
        FROM Sales
        GROUP BY product_id
    ) AS TEMP
        ON S.product_id = TEMP.product_id AND S.year = TEMP.first_year;
