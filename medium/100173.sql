-- 100173. Pizza Toppings Cost Analysis

SELECT
    CONCAT_WS (
        ",",
        t1.topping_name,
        t2.topping_name,
        t3.topping_name
    ) AS pizza,
    ROUND(t1.cost + t2.cost + t3.cost, 2) AS total_cost
FROM
    Toppings AS t1
    JOIN Toppings AS t2 ON t1.topping_name < t2.topping_name
    JOIN Toppings AS t3 ON t2.topping_name < t3.topping_name
    AND t1.topping_name < t3.topping_name
ORDER BY
    total_cost DESC,
    pizza ASC;
