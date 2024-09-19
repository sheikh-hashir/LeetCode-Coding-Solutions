# Intuition
- The goal is to remove duplicate entries from the `Person` table based on the `email` column while keeping the record with the smallest `id`. The duplicates are identified by checking for matching emails, and we can safely delete entries where the `id` is larger than that of another row with the same email.
<!-- Describe your first thoughts on how to solve this problem. -->

# Approach
- **Identify Duplicates:**
  - We use a `WITH` clause (Common Table Expression, or CTE) to identify the `ids` of duplicate rows.
  - Specifically, we perform a self-join on `the` Person table based on the `email` column, ensuring that we retain the record with the smallest id by filtering with `p.id > p1.id`.

- **Delete Duplicates:**
  - After identifying the duplicate rows, we delete them using the `DELETE` statement. The `WHERE id IN (...)` clause matches the ids from the CTE, ensuring only the duplicate entries are deleted.
<!-- Describe your approach to solving the problem. -->

# Code
```mysql []
WITH DuplicateIds AS (
    SELECT p.id
    FROM Person p
    INNER JOIN Person p1 ON p.email = p1.email
    WHERE p.id > p1.id
)
DELETE FROM Person
WHERE id IN (SELECT id FROM DuplicateIds);
```