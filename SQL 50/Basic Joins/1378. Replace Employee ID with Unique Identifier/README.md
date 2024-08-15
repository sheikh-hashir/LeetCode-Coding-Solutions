# Intuition
When dealing with two tables, `Employees` and `EmployeeUNI`, we often need to retrieve information from both tables, even when there are mismatches. Specifically, we want to list all employees and include their unique IDs from `EmployeeUNI` if they exist. This naturally suggests a `LEFT JOIN`.
<!-- Describe your first thoughts on how to solve this problem. -->

# Approach
- **LEFT JOIN:**
  - Use a `LEFT JOIN` to include all records from the `Employees` table and the matching records from the `EmployeeUNI` table.
- **SELECT Statement:**
  - Select the desired fields, which are the unique ID from `EmployeeUNI` and the name from `Employees`.
- **Alias for Tables:**
  - Use aliases for tables to simplify the query and make it more readable.


- `LEFT JOIN` ensures that every record from the `Employees` table is included in the result.
- If an employee does not have a matching unique ID in `EmployeeUNI`, the `unique_id` field will be `NULL`.
- This approach guarantees that no employees are excluded from the results.
<!-- Describe your approach to solving the problem. -->

# Code
```
# Write your MySQL query statement below
select eu.unique_id, e.name from Employees e left join EmployeeUNI eu ON e.id = eu.id

```