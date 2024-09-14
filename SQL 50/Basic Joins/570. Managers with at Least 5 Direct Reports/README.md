# Intuition
- To identify employees who manage at least five subordinates, we need to count the number of employees each manager is responsible for and filter out those with fewer than five subordinates.
<!-- Describe your first thoughts on how to solve this problem. -->

# Approach
- **Join Employee Table with Itself:**
  - Use a self join to pair each employee with their manager.
- **Group By Manager ID:**
  - Group the results by the manager's ID to aggregate the count of subordinates.
- **Filter by Count:**
  - Use the `HAVING` clause to filter groups with five or more subordinates.
<!-- Describe your approach to solving the problem. -->


# Code
```
# Write your MySQL query statement below
SELECT e.name FROM Employee e INNER JOIN Employee e1 ON e.id = e1.managerId GROUP BY e.id HAVING count(e1.managerId) >= 5;

```