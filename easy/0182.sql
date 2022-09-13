"""
182. Duplicate Emails
"""

-- Runtime: 631 ms, faster than 22.33% of MySQL online submissions for Duplicate Emails.
SELECT email AS "Email"
FROM Person
GROUP BY email HAVING count(id) > 1;
