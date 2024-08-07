# Intuition
- The task is to calculate the average years of experience for employees working on each project.
- We need to aggregate the experience data for each project and then compute the average.
<!-- Describe your first thoughts on how to solve this problem. -->

# Approach
- Join the `Employee` table with the Project table on the `employee_id`.
- For each `project_id`, sum the years of experience and count the number of employees.
- Divide the total years of experience by the number of employees to get the average.
- Round the result to 2 decimal places.
- Group the results by `project_id` to get the average years of experience for each project.
<!-- Describe your approach to solving the problem. -->

# Code
```
# Write your MySQL query statement below
SELECT project_id, ROUND(SUM(e.experience_years)/COUNT(p.project_id), 2) AS average_years FROM Employee e INNER JOIN Project p ON e.employee_id = p.employee_id GROUP BY p.project_id
```