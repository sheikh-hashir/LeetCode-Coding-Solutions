# Intuition
- When solving this problem, the goal is to find a specific number in a dataset based on given conditions.
- For example, if a number appears more than once, we should return `NULL`, otherwise return the number.
<!-- Describe your first thoughts on how to solve this problem. -->

# Approach
- **Grouping and Counting:** Group all numbers and count their occurrences.
- **Conditionally Returning Values:** If a number appears more than once, return `NULL`, otherwise return the number.
- **Sorting:** Sort the results in descending order.
- **Limiting Results:** Finally, limit the output to return only the top result.
<!-- Describe your approach to solving the problem. -->

# Code
```mysql []
# Write your MySQL query statement below
SELECT IF(COUNT(num) > 1, NULL, num) AS num
FROM MyNumbers
GROUP BY num
ORDER BY num DESC
LIMIT 1;
```