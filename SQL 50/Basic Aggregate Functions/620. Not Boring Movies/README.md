# Intuition
- The goal is to filter out movies with odd IDs that are not boring and sort them by their rating in descending order.

<!-- Describe your first thoughts on how to solve this problem. -->

# Approach
- Select movies with odd IDs using `id % 2 = 1`.
- Exclude movies with the description "boring".
- Sort the resulting movies by their rating in descending order.
<!-- Describe your approach to solving the problem. -->

# Code
```
# Write your MySQL query statement below
SELECT * FROM Cinema WHERE id % 2 = 1 and description != "boring" ORDER BY rating DESC
```