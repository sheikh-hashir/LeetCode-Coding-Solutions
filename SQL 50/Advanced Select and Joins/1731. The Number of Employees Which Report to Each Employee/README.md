# Intuition
- The task is to compute the number of direct reports and their average age for each manager in the employee hierarchy.
- We need to join the employee table with itself to identify the direct reports and then aggregate the data to compute the count and average age.
<!-- Describe your first thoughts on how to solve this problem. -->

# Approach
- **Self-Join:**
  - The `Employees` table is self-joined to match employees with their managers. This is done by joining the table where an employee's `reports_to` field matches another employee's `employee_id`.

- **Aggregation:**
  - **Count:**
    - For each manager, we count how many direct reports they have by using `COUNT(e1.reports_to)`.
  - **Average Age:**
    - We calculate the average age of the direct reports by summing up their ages and dividing it by the count of their ages, and rounding off the result.

- **Filtering:**
  - We filter the result set to only include managers who have at least one direct report using the `HAVING` clause.

- **Sorting:**
  - The final result is ordered by `employee_id` for a neat presentation.
<!-- Describe your approach to solving the problem. -->

# Code
```mysql []
# Write your MySQL query statement below
SELECT e.employee_id,
       e.name,
       Count(e1.reports_to)               AS reports_count,
       Round(Sum(e1.age) / Count(e1.age)) AS average_age
FROM   employees e
       INNER JOIN employees e1
               ON e.employee_id = e1.reports_to
GROUP  BY e.employee_id
HAVING Count(e1.reports_to) >= 1
ORDER BY e.employee_id;
```