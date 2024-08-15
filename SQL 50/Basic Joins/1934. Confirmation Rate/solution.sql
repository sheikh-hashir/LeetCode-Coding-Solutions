SELECT
    s.user_id,
    CASE
        WHEN SUM(c.action = "confirmed") > 0 THEN ROUND(SUM(c.action = "confirmed")/COUNT(*), 2)
    ELSE 0 END as confirmation_rate
FROM Signups s LEFT JOIN Confirmations c ON s.user_id = c.user_id GROUP BY s.user_id;
