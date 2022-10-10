-- 1581. Customer Who Visited but Did Not Make Any Transactions

SELECT customer_id, COUNT(Visits.visit_id) AS count_no_trans
FROM Visits
    LEFT JOIN Transactions ON Visits.visit_id = Transactions.visit_id
WHERE transaction_id IS NULL
GROUP BY customer_id;
