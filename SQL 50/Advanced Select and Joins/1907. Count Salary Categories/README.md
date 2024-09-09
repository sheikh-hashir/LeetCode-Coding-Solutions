# Intuition
- To categorize and count the number of accounts based on income ranges (low, average, and high), the solution groups incomes into predefined categories and calculates the number of accounts within each category.
<!-- Describe your first thoughts on how to solve this problem. -->

# Approach
- Use a `SELECT` statement with `IF` conditions to categorize income into `"Low Salary,"` `"Average Salary,"` and `"High Salary."`
- Use the `SUM(IF(...))` construct to count accounts in each income category.
- Use `UNION` to combine the results of three separate queries for each category into a single result set.
<!-- Describe your approach to solving the problem. -->

# Code
```mysql []
# Write your MySQL query statement below
SELECT "Low Salary" AS category, SUM(IF(income<20000,1,0)) accounts_count FROM Accounts UNION
SELECT "Average Salary" AS category, SUM(IF((income>=20000 and income<=50000),1,0)) accounts_count FROM Accounts UNION
SELECT "High Salary" AS category, SUM(IF(income>50000,1,0)) accounts_count FROM Accounts

```