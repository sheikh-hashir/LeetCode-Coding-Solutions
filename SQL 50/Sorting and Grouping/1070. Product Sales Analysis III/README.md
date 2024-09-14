# Intuition
- The goal is to find the details of the first sale for each product based on the earliest year of sale.
<!-- Describe your first thoughts on how to solve this problem. -->

# Approach
- Identifying the earliest year of sale for each product using a subquery.
- Using the subquery in the `WHERE` clause to filter the results and get the corresponding product details from the main `Sales` table.
<!-- Describe your approach to solving the problem. -->

# Explanation
- **Subquery:**
  - The subquery finds the minimum year of sale for each product.
- **Main Query:**
  - The main query retrieves all columns for the sales that correspond to the earliest year per product, as identified by the subquery.

# Code
```mysql []
SELECT
    product_id, year AS first_year, quantity, price
FROM
    Sales
WHERE
    (product_id, year) IN (
        SELECT
            product_id, MIN(year)
        FROM
            Sales
        GROUP BY product_id
    );

```