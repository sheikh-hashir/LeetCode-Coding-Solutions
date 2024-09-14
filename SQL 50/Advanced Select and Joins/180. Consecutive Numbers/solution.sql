SELECT
    DISTINCT ((SELECT num FROM Logs WHERE id = l.id)) AS ConsecutiveNums
FROM
    Logs l
WHERE
    (SELECT num FROM Logs WHERE id = l.id) = (SELECT num FROM Logs WHERE id = l.id + 1)
    AND (SELECT num FROM Logs WHERE id = l.id) = (SELECT num FROM Logs WHERE id = l.id + 2);
