# Intuition
- This query aims to fetch two results:
  - The user who has provided the most movie ratings.
  - The highest-rated movie for a specific time period.

<!-- Describe your first thoughts on how to solve this problem. -->

# Approach
- The query is split into two parts:
  - The first part retrieves the user who has provided the most ratings. It uses `GROUP BY` to group by user and orders by the count of ratings in descending order.
  - The second part retrieves the movie with the highest average rating during a specified time range. It filters by a date range and groups by the movie, ordering by the highest average rating.

`UNION ALL` is used to combine both results into one output.
<!-- Describe your approach to solving the problem. -->

# Code
```mysql []
(SELECT u.name AS results
 FROM Users u
 INNER JOIN MovieRating mr ON u.user_id = mr.user_id
 INNER JOIN Movies m ON m.movie_id = mr.movie_id
 GROUP BY u.user_id
 ORDER BY COUNT(mr.rating) DESC, u.name
 LIMIT 1)

UNION ALL

(SELECT m.title AS results
 FROM Movies m
 INNER JOIN MovieRating mr ON m.movie_id = mr.movie_id
 WHERE mr.created_at >='2020-02-01' and mr.created_at < '2020-03-01'
 GROUP BY mr.movie_id
 ORDER BY AVG(mr.rating) DESC, m.title
 LIMIT 1);

```