-- 3521. Find Product Recommendation Pairs

SELECT
    product1_id,
    product2_id,
    I1.category AS product1_category,
    I2.category AS product2_category,
    customer_count
FROM
    (
        SELECT
            P1.product_id AS product1_id,
            P2.product_id AS product2_id,
            count(DISTINCT P1.user_id) AS customer_count
        FROM
            ProductPurchases AS P1
            JOIN ProductPurchases AS P2 ON P1.user_id = P2.user_id
            AND P1.product_id < P2.product_id
        GROUP BY
            P1.product_id,
            P2.product_id
        HAVING
            customer_count >= 3
    ) AS TBL
    JOIN ProductInfo AS I1 ON TBL.product1_id = I1.product_id
    JOIN ProductInfo AS I2 ON TBL.product2_id = I2.product_id
ORDER BY
    customer_count DESC,
    product1_id ASC,
    product2_id ASC;
