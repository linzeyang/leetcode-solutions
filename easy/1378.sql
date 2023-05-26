-- 1378. Replace Employee ID With The Unique Identifier

SELECT unique_id, name
FROM EmployeeUNI
    RIGHT JOIN Employees
    ON EmployeeUNI.id = Employees.id;
