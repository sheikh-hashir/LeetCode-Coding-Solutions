SELECT e.name FROM Employee e INNER JOIN Employee e1 ON e.id = e1.managerId GROUP BY e.id HAVING count(e1.managerId) >= 5;
