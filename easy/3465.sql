-- 3465. Find Products with Valid Serial Numbers

SELECT
    *
FROM
    products
WHERE
    description REGEXP "^.*SN\\d{4}-\\d{4}\\D*$"
ORDER BY
    product_id ASC;
