SELECT (SELECT DISTINCT salary
        FROM   employee
        ORDER  BY salary DESC
        LIMIT  1 offset 1) AS SecondHighestSalary;
