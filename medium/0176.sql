-- 176. Second Highest Salary

SELECT (
    SELECT salary
    FROM Employee
    WHERE salary < (
        SELECT max(salary)
        FROM Employee
    )
    ORDER BY salary DESC
    LIMIT 1
) AS SecondHighestSalary;
