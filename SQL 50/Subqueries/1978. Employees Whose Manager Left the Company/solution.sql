SELECT e.employee_id
FROM   employees e
WHERE  e.salary < 30000
       AND e.manager_id IS NOT NULL
       AND NOT EXISTS(SELECT 1
                      FROM   employees sub
                      WHERE  sub.employee_id = e.manager_id)
ORDER  BY e.employee_id