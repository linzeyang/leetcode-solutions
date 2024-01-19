"""197. Rising Temperature"""

SELECT t1.id
FROM Weather AS t1
INNER JOIN Weather AS t2
    ON t1.recordDate = t2.recordDate + INTERVAL 1 DAY
WHERE t1.temperature > t2.temperature;
