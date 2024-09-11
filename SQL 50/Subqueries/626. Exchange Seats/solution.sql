SELECT s.id,
       CASE
         WHEN s.id % 2 = 0 THEN (SELECT student
                                 FROM   Seat
                                 WHERE  id = s.id - 1)
         ELSE IFNULL((SELECT student
                      FROM   Seat
                      WHERE  id = s.id + 1), s.student)
       END student
FROM   Seat s