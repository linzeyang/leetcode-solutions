"""
197. Rising Temperature
"""

-- Slow:
-- Runtime: 809 ms, faster than 25.37% of MySQL online submissions for Rising Temperature.
SELECT t1.id
FROM Weather AS t1
INNER JOIN Weather AS t2
    ON t1.recordDate = t2.recordDate + INTERVAL 1 DAY
WHERE t1.temperature > t2.temperature;
