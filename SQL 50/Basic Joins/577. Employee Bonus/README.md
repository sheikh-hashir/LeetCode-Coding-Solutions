# Intuition
- We need to retrieve employee names and their bonuses, but only include those with bonuses less than 1000.
- If an employee does not have a bonus, treat their bonus as 0.


<!-- Describe your first thoughts on how to solve this problem. -->

# Approach
- **Join Tables:**
  - Use a `LEFT JOIN` to include all employees, even those without bonuses.
- **Handle NULL Values:**
  - Use the `COALESCE` function to treat `NULL` bonuses as 0.
- **Filter Results:**
  - Filter the results to include only those with bonuses less than 1000.

<!-- Describe your approach to solving the problem. -->

# Code
```
# Write your MySQL query statement below
SELECT e.name, b.bonus FROM Employee e LEFT JOIN Bonus b ON e.empID = b.empID where COALESCE(b.bonus, 0) < 1000;

```