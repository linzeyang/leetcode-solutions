"""
196. Delete Duplicate Emails
"""

-- Runtime: 611 ms, faster than 91.88% of MySQL online submissions for Delete Duplicate Emails.
DELETE FROM Person
WHERE id not in (
    SELECT * FROM (
        SELECT MIN(id) FROM Person GROUP BY email
    ) AS TEMP
);
