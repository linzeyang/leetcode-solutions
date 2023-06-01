-- 1280. Students and Examinations

SELECT
    ST.student_id,
    ST.student_name,
    SU.subject_name,
    COUNT(EX.subject_name) AS attended_exams
FROM Students AS ST
    JOIN Subjects AS SU
    LEFT JOIN Examinations AS EX
        ON ST.student_id = EX.student_id AND SU.subject_name = EX.subject_name
GROUP BY ST.student_id, SU.subject_name
ORDER BY ST.student_id, SU.subject_name;
