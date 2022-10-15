-- 626. Exchange Seats

SELECT
CASE
    WHEN MOD(Seat.id, 2) = 0 THEN Seat.id - 1
    WHEN Seat.id = (SELECT COUNT(Seat.id) FROM Seat) THEN Seat.id
    WHEN MOD(Seat.id, 2) = 1 THEN Seat.id + 1
END AS id,
student
FROM Seat
ORDER BY id ASC;
