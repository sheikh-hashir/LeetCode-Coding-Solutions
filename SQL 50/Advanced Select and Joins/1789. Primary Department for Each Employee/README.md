# Intuition
- The task involves assigning a department to each employee based on certain conditions.
- If an employee is only associated with one department, we simply return that department.
- However, if the employee is associated with multiple departments, we need to check which one is marked as their primary department.
<!-- Describe your first thoughts on how to solve this problem. -->

# Approach
- **Grouping:**
  - Group the data by `employee_id` to handle each employee separately.
- **Conditional Selection:**
  - Use the `CASE` statement to decide which department_id to return:
    - If the employee is linked to exactly one department, return that department.
    - If the employee is linked to multiple departments, return the department where `primary_flag = 'Y'`.
- **Subquery:**
  - The subquery retrieves the primary department for employees associated with multiple departments.
<!-- Describe your approach to solving the problem. -->

# Code
```mysql []
SELECT
    e.employee_id,
    CASE
        WHEN COUNT(e.employee_id) = 1 THEN e.department_id
        ELSE (
            SELECT department_id
            FROM Employee
            WHERE employee_id = e.employee_id
            AND primary_flag = 'Y'
        )
    END AS department_id
FROM
    Employee e
GROUP BY
    e.employee_id;

```