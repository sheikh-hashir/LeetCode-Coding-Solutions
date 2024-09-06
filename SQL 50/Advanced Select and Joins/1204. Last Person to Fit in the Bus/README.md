# Intuition
- The problem requires selecting the person whose cumulative weight in the queue does not exceed a given threshold.
- This involves grouping the queue data and summing weights to determine the most optimal person within the constraint.
<!-- Describe your first thoughts on how to solve this problem. -->

# Approach
- Use a `LEFT JOIN` to create a cumulative sum of weights for people in the queue.
- Group by the person's name to calculate the total weight for each individual up to that point.
- Apply a condition in the `HAVING` clause to filter out people whose cumulative weight exceeds `1000`.
- Order the results by the cumulative weight in descending order and limit the results to the person who reaches the highest total weight without exceeding the threshold.
<!-- Describe your approach to solving the problem. -->

# Code
```mysql []
SELECT q.person_name
FROM   queue q
       LEFT JOIN queue q1
              ON q.turn >= q1.turn
GROUP  BY q.person_name
HAVING SUM(q1.weight) <= 1000
ORDER  BY SUM(q1.weight) DESC LIMIT 1
```