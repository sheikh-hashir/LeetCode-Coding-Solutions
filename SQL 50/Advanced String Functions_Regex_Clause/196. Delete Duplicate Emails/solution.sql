WITH DuplicateIds AS (
    SELECT p.id
    FROM Person p
    INNER JOIN Person p1 ON p.email = p1.email
    WHERE p.id > p1.id
)
DELETE FROM Person
WHERE id IN (SELECT id FROM DuplicateIds);