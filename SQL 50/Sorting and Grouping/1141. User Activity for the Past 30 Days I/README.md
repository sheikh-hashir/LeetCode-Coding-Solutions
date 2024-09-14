# Intuition
- The task is to determine the number of distinct users who were active on each day within a given period. By grouping the results by `activity_date`, we can summarize daily user activity.
<!-- Describe your first thoughts on how to solve this problem. -->

# Approach
- `Group by Date:`
  - Group the records by `activity_date` to calculate the active users for each specific day.
- **Count Distinct Users:**
  - Use `COUNT(DISTINCT user_id)` to ensure that each user is only counted once per day.
- **Filter Date Range:**
  - Apply the `HAVING` clause to limit the results to the dates between `'2019-06-28'` and `'2019-07-27'`.
<!-- Describe your approach to solving the problem. -->

# Code
```
# Write your MySQL query statement below
SELECT activity_date AS day, COUNT(DISTINCT user_id) AS active_users FROM Activity GROUP BY activity_date HAVING activity_date BETWEEN '2019-06-28' and '2019-07-27'
```