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