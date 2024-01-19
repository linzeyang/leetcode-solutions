"""182. Duplicate Emails"""

SELECT email AS "Email"
FROM Person
GROUP BY email HAVING count(id) > 1;
