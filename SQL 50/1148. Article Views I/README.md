# Intuition
- The task is to retrieve distinct author IDs from the `Views` table where the author is also the viewer and sort these IDs in ascending order.
<!-- Describe your first thoughts on how to solve this problem. -->

# Approach
- **Filter Rows:**
  - Use a `WHERE` clause to filter rows where `author_id` is equal to `viewer_id`.
- **Select Distinct Values:**
  - Use `SELECT DISTINCT` to retrieve unique `author_id` values that meet the condition.
- **Alias the Column:**
  - Use `AS` to alias the selected `author_id` as `id` for clarity in the result set.
- **Sort the Results:**
   - Use `ORDER BY author_id` to sort the results in ascending order.
<!-- Describe your approach to solving the problem. -->

# Code
```
# Write your MySQL query statement below
SELECT DISTINCT(author_id) as id from Views WHERE author_id = viewer_id ORDER BY author_id;

```