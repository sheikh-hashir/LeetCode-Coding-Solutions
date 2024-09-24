# Intuition
- The task aims to retrieve product names along with their total units sold during a specific date range.
- Additionally, only products with total units greater than or equal to 100 should be included.
<!-- Describe your first thoughts on how to solve this problem. -->

# Approach

- **Subquery to Filter Orders:**
  - A subquery is used to first filter out all orders placed between the given date range (`2020-02-01` to `2020-02-29`).
  - This subquery joins the `products` and `orders` tables using the `product_id` to access both product names and order details.

- **Group By and Aggregation:**
  - After filtering, the main query groups the result by `product_id` and calculates the sum of units sold for each product.
  - The `HAVING` clause ensures that only products with a sum of units greater than or equal to 100 are included in the final result.
<!-- Describe your approach to solving the problem. -->

# Code
```mysql []
SELECT product_name,
       Sum(unit) AS unit
FROM   (SELECT p.product_name,
               o.unit,
               p.product_id
        FROM   products p
               INNER JOIN orders o
                       ON p.product_id = o.product_id
        WHERE  o.order_date BETWEEN '2020-02-01' AND '2020-02-29') AS dummy
GROUP  BY product_id
HAVING Sum(unit) >= 100
```