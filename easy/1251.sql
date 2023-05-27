-- 1251. Average Selling Price

SELECT
    p.product_id AS product_id,
    ROUND(SUM(p.price * u.units) / SUM(units), 2) AS average_price
FROM Prices AS p
    JOIN UnitsSold AS u
        ON p.product_id = u.product_id
            AND u.purchase_date >= p.start_date
            AND u.purchase_date <= end_date
GROUP BY p.product_id;
