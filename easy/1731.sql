-- 1731. The Number of Employees Which Report to Each Employee

SELECT
    E1.employee_id,
    E1.name,
    COUNT(E2.employee_id) AS reports_count,
    ROUND(AVG(E2.age), 0) AS average_age
FROM
    Employees AS E1
    JOIN Employees AS E2 ON E1.employee_id = E2.reports_to
GROUP BY
    E1.employee_id
ORDER BY
    E1.employee_id;
