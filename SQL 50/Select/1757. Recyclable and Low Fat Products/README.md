# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
The task is to retrieve all the products that are both low in fats and recyclable.

# Approach
- **Query the Database:**
  - Use a SQL `SELECT` statement to fetch the `product_id` from the `Products` table.
  - **Filter Conditions:** Apply `WHERE` clauses to filter products where both `low_fats` is '`Y`' and `recyclable` is '`Y`'.
<!-- Describe your approach to solving the problem. -->

# Code
```
# Write your MySQL query statement below
select product_id from Products where low_fats = 'Y' and recyclable = "Y"

```