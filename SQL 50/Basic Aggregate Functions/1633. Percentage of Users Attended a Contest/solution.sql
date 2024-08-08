SELECT r.contest_id,
       Round(( Count(r.contest_id) / (SELECT Count(user_id)
                                      FROM   users) * 100 ), 2) AS percentage
FROM   users u
       INNER JOIN register r
               ON u.user_id = r.user_id
GROUP  BY r.contest_id
ORDER  BY percentage DESC,
          r.contest_id