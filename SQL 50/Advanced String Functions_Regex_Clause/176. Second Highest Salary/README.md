# Intuition
- To solve the problem of finding the second highest salary in an Employee table, we need to focus on ordering the salaries in descending order and selecting the second unique salary.
- If there is no second highest salary, the result should return `NULL`.
- This ensures the solution is flexible enough to handle cases where there is only one distinct salary or no employees at all.
<!-- Describe your first thoughts on how to solve this problem. -->

# Approach
- First, we need to order the salaries in descending order so that the highest salary appears first.
- Then, we skip the first result (which is the highest salary) using the `OFFSET 1` clause to retrieve the second distinct salary.
- In case there is no second salary, the query will return `NULL`.
- We use `DISTINCT` to ensure we are working with unique salary values, avoiding issues with duplicate salaries.
- The subquery ensures that we only return the second highest salary as the result.
<!-- Describe your approach to solving the problem. -->

# Code
```mysql []
# Write your MySQL query statement below
SELECT (SELECT DISTINCT salary
        FROM   employee
        ORDER  BY salary DESC
        LIMIT  1 offset 1) AS SecondHighestSalary;

```