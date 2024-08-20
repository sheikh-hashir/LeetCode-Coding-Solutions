# Intuition
- The problem is asking to determine the number of unique subjects taught by each teacher. This can be accomplished by counting the distinct `subject_id` for each `teacher_id`.
<!-- Describe your first thoughts on how to solve this problem. -->

# Approach
- Use the `GROUP BY` clause to group the data by `teacher_id` so that each group contains the data related to a single teacher.
- For each group, count the distinct `subject_id` values to get the number of unique subjects taught by that teacher.
- The `COUNT(DISTINCT subject_id)` function is used to ensure only unique subject IDs are counted for each teacher.
<!-- Describe your approach to solving the problem. -->

# Code
```
# Write your MySQL query statement below
SELECT teacher_id, COUNT(DISTINCT subject_id) AS cnt FROM Teacher GROUP BY teacher_id;
```
