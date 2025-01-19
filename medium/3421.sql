-- 3421. Find Students Who Improved

WITH FirstScores AS (
    SELECT
        student_id,
        subject,
        score AS first_score,
        exam_date AS first_exam_date
    FROM
        Scores
    WHERE
        (student_id, subject, exam_date) IN (
            SELECT
                student_id,
                subject,
                MIN(exam_date)
            FROM
                Scores
            GROUP BY
                student_id,
                subject
        )
),
LatestScores AS (
    SELECT
        student_id,
        subject,
        score AS latest_score,
        exam_date AS latest_exam_date
    FROM
        Scores
    WHERE
        (student_id, subject, exam_date) IN (
            SELECT
                student_id,
                subject,
                MAX(exam_date)
            FROM
                Scores
            GROUP BY
                student_id,
                subject
        )
)
SELECT
    F.student_id,
    F.subject,
    F.first_score,
    L.latest_score
FROM
    FirstScores F
    JOIN LatestScores L ON F.student_id = L.student_id
    AND F.subject = L.subject
WHERE
    L.latest_score > F.first_score
ORDER BY
    F.student_id,
    F.subject;
