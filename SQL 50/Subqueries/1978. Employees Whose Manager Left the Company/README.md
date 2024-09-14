# Intuition
- This query retrieves the IDs of employees who earn less than 30,000, have a manager, but whose manager does not have any subordinates.
- The query uses a subquery with `NOT EXISTS` to check that no employees have the same `employee_id` as the given employee's `manager_id`, ensuring that the manager has no subordinates.
<!-- Describe your first thoughts on how to solve this problem. -->

# Approach
- **Salary Condition:**
  - Only employees with a salary less than 30,000 are selected.
- **Manager Condition:**
  - The query filters out employees without a manager (`e.manager_id IS NOT NULL`).
- **Subordinate Check:**
  - The `NOT EXISTS` clause ensures that no other employees are linked to the given employee's manager.
<!-- Describe your approach to solving the problem. -->


# Code
```mysql []
SELECT e.employee_id
FROM   employees e
WHERE  e.salary < 30000
       AND e.manager_id IS NOT NULL
       AND NOT EXISTS(SELECT 1
                      FROM   employees sub
                      WHERE  sub.employee_id = e.manager_id)
ORDER  BY e.employee_id
```