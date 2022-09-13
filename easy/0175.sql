"""
175. Combine Two Tables
"""

-- Runtime: 571 ms, faster than 35.25% of MySQL online submissions for Combine Two Tables
SELECT firstName, lastName, city, state
FROM Person
LEFT OUTER JOIN Address ON Person.personId = Address.personId 
WHERE 1;
