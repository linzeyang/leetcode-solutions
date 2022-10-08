-- 620. Not Boring Movies

SELECT id, movie, description, rating
FROM Cinema
WHERE description <> "boring" AND MOD(id, 2) = 1
ORDER BY rating DESC;
