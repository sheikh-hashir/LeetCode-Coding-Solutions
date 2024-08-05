# Intuition
- To combine product information with sales data, we need to join the `Product` and `Sales` tables using a common field.
- This will allow us to retrieve the product name along with the corresponding sales year and price.
<!-- Describe your first thoughts on how to solve this problem. -->

# Approach
- **INNER JOIN:**
  - Use an `INNER JOIN` to combine rows from `Product` and `Sales` tables based on the common `product_id` field.
- **Select Necessary Columns:**
  - Choose the `product_name` from the `Product` table and `year` and `price` from the `Sales` table.
<!-- Describe your approach to solving the problem. -->

# Code
```
# Write your MySQL query statement below
SELECT p.product_name, s.year, s.price FROM Product p INNER JOIN Sales s on s.product_id = p.product_id

```
