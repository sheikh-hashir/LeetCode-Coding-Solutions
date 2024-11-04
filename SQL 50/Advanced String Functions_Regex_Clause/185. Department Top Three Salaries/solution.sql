SELECT d.name    AS Department,
       e1.name   AS Employee,
       e1.salary AS Salary
FROM   Employee e1
       JOIN Department d
         ON e1.departmentId = d.id
WHERE  3 > (SELECT Count(DISTINCT ( e2.salary ))
            FROM   Employee e2
            WHERE  e2.salary > e1.salary
                   AND e1.departmentId = e2.departmentId)