"""196. Delete Duplicate Emails"""

DELETE FROM Person
WHERE id not in (
    SELECT * FROM (
        SELECT MIN(id) FROM Person GROUP BY email
    ) AS TEMP
);
