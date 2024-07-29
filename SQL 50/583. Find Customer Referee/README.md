# Intuition
- The task is to retrieve customer names where the `referee_id` is either not equal to `2` or is `NULL`.

# Approach
- **Use the `COALESCE` Function:**
  - Utilize `COALESCE` to replace `NULL` values with a default value (e.g., 0) to facilitate the comparison.
  - **Check Inequality:** Compare the result of `COALESCE(referee_id, 0)` with `2` to filter out the desired rows.
<!-- Describe your approach to solving the problem. -->

# Code
```
SELECT name FROM Customer WHERE COALESCE(referee_id, 0) != 2;
```