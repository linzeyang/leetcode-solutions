-- 1661. Average Time of Process per Machine

SELECT
    machine_id,
    ROUND(AVG(process_time), 3) AS processing_time
FROM
    (
        SELECT
            machine_id,
            process_id,
            ROUND(MAX(timestamp) - MIN(timestamp), 3) AS process_time
        FROM
            Activity
        GROUP BY
            machine_id,
            process_id
    ) AS TBL
GROUP BY
    machine_id;
