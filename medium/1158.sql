-- 1158. Market Analysis I

SELECT u.user_id AS buyer_id, u.join_date, IFNULL(TEMP.orders, 0) AS orders_in_2019
FROM Users AS u
    LEFT JOIN (
        SELECT user_id AS uid, count(order_id) AS orders
        FROM Users
            JOIN Orders ON user_id = buyer_id
        WHERE order_date BETWEEN "2019-01-01" AND "2020-01-01"
        GROUP BY user_id
    ) AS TEMP ON u.user_id = TEMP.uid;
