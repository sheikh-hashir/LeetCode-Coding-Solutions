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
