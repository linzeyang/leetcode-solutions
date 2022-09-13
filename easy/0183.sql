"""
183. Customers Who Never Order
"""

-- Runtime: 600 ms, faster than 46.67% of MySQL online submissions for Customers Who Never Order.
SELECT name AS "Customers"
FROM Customers
LEFT OUTER JOIN Orders
    ON Customers.id = Orders.customerId
WHERE Orders.id IS NULL;
