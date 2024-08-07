SELECT project_id, ROUND(SUM(e.experience_years)/COUNT(p.project_id), 2) AS average_years
    FROM Employee e INNER JOIN Project p ON e.employee_id = p.employee_id
GROUP BY p.project_id