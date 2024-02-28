-- 3051. Find Candidates for Data Scientist Position

SELECT
    TEMP.candidate_id AS candidate_id
FROM
    (
        SELECT
            candidate_id,
            GROUP_CONCAT (skill SEPARATOR ",") AS skills
        FROM
            candidates
        GROUP BY
            candidate_id
    ) AS TEMP
WHERE
    INSTR (TEMP.skills, "Python") > 0
    AND INSTR (TEMP.skills, "Tableau") > 0
    AND INSTR (TEMP.skills, "PostgreSQL") > 0
ORDER BY
    TEMP.candidate_id;
