-- 1527. Patients With a Condition

SELECT *
FROM Patients
WHERE LEFT(conditions, 5) = "DIAB1" OR INSTR(conditions, " DIAB1");
