# Intuition
- The problem involves calculating two metrics for each `query_name` in a database: the quality of the queries and the percentage of queries with a rating lower than 3.
- The challenge is to accurately compute these metrics while ensuring that `NULL` values in `query_name` are handled appropriately.
<!-- Describe your first thoughts on how to solve this problem. -->

# Approach
- Calculating the `quality` of a query by averaging the ratio of rating to position for each `query_name`.
- Determining the `poor_query_percentage`, which is the percentage of queries with a rating below 3 for each `query_name`.
- Using `GROUP BY` to group the results by `query_name`.
- Applying a `HAVING` clause to exclude rows where `query_name` is `NULL`, ensuring only valid names are included in the results.
<!-- Describe your approach to solving the problem. -->

# Code
```
# Write your MySQL query statement below
SELECT query_name,
       Round(Sum(q.rating / q.position) / (SELECT Count(*)
                                           FROM   queries
                                           WHERE  query_name = q.query_name), 2)
       AS
       quality,
       Round(( Sum(CASE
                     WHEN q.rating < 3 THEN 1
                     ELSE 0
                   end) / (SELECT Count(*)
                           FROM   queries
                           WHERE  query_name = q.query_name) * 100 ), 2)
       AS
       poor_query_percentage
FROM   queries q
GROUP  BY q.query_name HAVING q.query_name is not null
```