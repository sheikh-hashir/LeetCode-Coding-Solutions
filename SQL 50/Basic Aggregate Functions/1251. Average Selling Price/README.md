# Intuition
- To calculate the average price of products based on the units sold, we need to handle scenarios where some products might not have any sales data.
- By using a `LEFT JOIN`, we can ensure that all products are included in the result, even if they have no corresponding entries in the `UnitsSold` table.
<!-- Describe your first thoughts on how to solve this problem. -->

# Approach
- **Join Tables:**
  - Use a `LEFT JOIN` to include all products from the Prices table and any matching entries from the `UnitsSold` table based on `product_id` and within the date range specified.
- **Aggregation:**
  - Calculate the weighted average price using the `SUM` of the product of `price` and `units` divided by the `SUM` of `units`.
- **Handle NULLs:**
  - Use the `COALESCE` function to return 0 for products that have no sales data.
<!-- Describe your approach to solving the problem. -->

# Code
```
SELECT p.product_id,
    COALESCE(ROUND(SUM(p.price * u.units) / SUM(u.units), 2), 0) AS average_price
FROM Prices p
LEFT JOIN UnitsSold u ON p.product_id = u.product_id
    AND u.purchase_date >= p.start_date
    AND u.purchase_date <= p.end_date
GROUP BY p.product_id;

```