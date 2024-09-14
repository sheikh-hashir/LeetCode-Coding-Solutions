SELECT e.employee_id,
       e.name,
       Count(e1.reports_to)               AS reports_count,
       Round(Sum(e1.age) / Count(e1.age)) AS average_age
FROM   employees e
       INNER JOIN employees e1
               ON e.employee_id = e1.reports_to
GROUP  BY e.employee_id
HAVING Count(e1.reports_to) >= 1
ORDER BY e.employee_id;
