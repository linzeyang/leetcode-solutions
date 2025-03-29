-- 3497. Analyze Subscription Conversion

SELECT
    trial.user_id AS user_id,
    trial.avg_duration AS trial_avg_duration,
    paid.avg_duration AS paid_avg_duration
FROM
    (
        SELECT
            user_id,
            ROUND(AVG(activity_duration), 2) AS avg_duration
        FROM
            UserActivity
        WHERE
            activity_type = 'free_trial'
        GROUP BY
            user_id
    ) AS trial
    JOIN (
        SELECT
            user_id,
            ROUND(AVG(activity_duration), 2) AS avg_duration
        FROM
            UserActivity
        WHERE
            activity_type = 'paid'
        GROUP BY
            user_id
    ) AS paid ON trial.user_id = paid.user_id
ORDER BY
    trial.user_id ASC;
