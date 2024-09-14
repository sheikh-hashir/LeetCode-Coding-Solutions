Calculating User Confirmation Rates with Conditional Aggregation

# Intuition
- We need to calculate the confirmation rate for each user.
- The confirmation rate is defined as the ratio of confirmed actions to total actions for a user.
- If a user has no confirmed actions, their confirmation rate should be 0.
<!-- Describe your first thoughts on how to solve this problem. -->

# Approach
- Perform a left join between the `Signups` table and the `Confirmations` table based on `user_id`.
- Use the `CASE` statement to compute the confirmation rate:
  - If there are confirmed actions (`SUM(c.action = "confirmed") > 0`), calculate the ratio of confirmed actions to total actions and round it to 2 decimal places.
  - If there are no confirmed actions, set the confirmation rate to 0.
- Group the results by `user_id`.
<!-- Describe your approach to solving the problem. -->

# Code
```
# Write your MySQL query statement below
SELECT
    s.user_id,
    CASE
        WHEN SUM(c.action = "confirmed") > 0 THEN ROUND(SUM(c.action = "confirmed")/COUNT(*), 2)
    ELSE 0 END as confirmation_rate
FROM Signups s LEFT JOIN Confirmations c ON s.user_id = c.user_id GROUP BY s.user_id

```