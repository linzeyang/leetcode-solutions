-- 1965. Employees With Missing Information

SELECT e.employee_id AS employee_id
FROM Employees AS e
LEFT JOIN Salaries AS s ON e.employee_id = s.employee_id
WHERE s.salary IS NULL
UNION
SELECT s.employee_id AS employee_id
FROM Employees AS e
RIGHT JOIN Salaries AS s ON e.employee_id = s.employee_id
WHERE e.name IS NULL
ORDER BY employee_id ASC;
