SELECT e.name, b.bonus FROM Employee e LEFT JOIN Bonus b ON e.empID = b.empID where COALESCE(b.bonus, 0) < 1000;
