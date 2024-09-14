SELECT q.person_name
FROM   queue q
       LEFT JOIN queue q1
              ON q.turn >= q1.turn
GROUP  BY q.person_name
HAVING SUM(q1.weight) <= 1000
ORDER  BY SUM(q1.weight) DESC LIMIT 1;
