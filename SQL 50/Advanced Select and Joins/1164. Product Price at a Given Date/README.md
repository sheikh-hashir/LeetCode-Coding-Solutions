# Intuition
- The goal is to retrieve the most recent `new_price` for each product before or on a given date, or return a default value if no price exists.
- This requires leveraging subqueries to extract the latest price and using fallback logic for cases where no price is available.
<!-- Describe your first thoughts on how to solve this problem. -->

# Approach
- **Subquery:**
  - For each product, find the latest price (based on `change_date`) on or before `2019-08-16`.
- **COALESCE:**
  - Use `COALESCE` to return the found price, or default to `10` if no price is available.
- **Grouping:**
  - Group the query by `product_id` to ensure unique products are retrieved.
<!-- Describe your approach to solving the problem. -->

# Code
```mysql []
SELECT
    p.product_id,
    COALESCE(
        (SELECT new_price
         FROM Products
         WHERE change_date <= '2019-08-16'
         AND product_id = p.product_id
         ORDER BY change_date DESC
         LIMIT 1),
        10
    ) AS price
FROM
    Products p
GROUP BY
    p.product_id;
```