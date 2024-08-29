# Intuition
- The problem involves finding consecutive numbers in a log table. We need to check if a certain number appears consecutively in three consecutive rows.
- If the condition is met, the number should be included in the result.
<!-- Describe your first thoughts on how to solve this problem. -->

# Approach
- We use a `SELECT` query to compare the num values of three consecutive rows.
- We use subqueries to check the values of the current row and the next two rows.
- If all three values are equal, the number is considered a "consecutive number," and it is included in the result.
- To avoid duplicates, we use the `DISTINCT` keyword.
<!-- Describe your approach to solving the problem. -->

# Code
```mysql []
SELECT
    DISTINCT ((SELECT num FROM Logs WHERE id = l.id)) AS ConsecutiveNums
FROM
    Logs l
WHERE
    (SELECT num FROM Logs WHERE id = l.id) = (SELECT num FROM Logs WHERE id = l.id + 1)
    AND (SELECT num FROM Logs WHERE id = l.id) = (SELECT num FROM Logs WHERE id = l.id + 2);

```