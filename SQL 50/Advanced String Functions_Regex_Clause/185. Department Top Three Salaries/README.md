# Intuition
- The task is to find the top 3 highest-paid employees in each department.
- For each employee, we want to see if their salary is among the top 3 within their department by comparing their salary to others in the same department.
<!-- Describe your first thoughts on how to solve this problem. -->

# Approach
- Join the `Employee` table with the `Department` table using the `departmentId`.
- For each employee, use a `subquery` to count how many employees in the same department have a higher salary. We want to find employees whose salary ranks in the top 3.
- The subquery ensures that for each employee, we count how many employees in the same department have a higher salary, and only include those for which fewer than 3 employees have higher salaries.
<!-- Describe your approach to solving the problem. -->

# Code
```mysql []
# Write your MySQL query statement below
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
```
