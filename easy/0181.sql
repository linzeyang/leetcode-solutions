"""181. Employees Earning More Than Their Managers"""

SELECT t1.name AS "Employee"
FROM Employee AS t1
INNER JOIN Employee AS t2 ON t1.managerId  = t2.id
WHERE t1.salary > t2.salary;
