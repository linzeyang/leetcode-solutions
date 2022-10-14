-- 184. Department Highest Salary

SELECT d.name AS Department, e.name AS Employee, e.salary AS salary
FROM Employee AS e
JOIN Department AS d ON e.departmentId = d.id
JOIN (
    SELECT departmentId AS did, MAX(salary) AS max_salary
    FROM Employee
    GROUP BY did
) AS TEMP ON e.departmentId = TEMP.did AND e.salary = TEMP.max_salary;
