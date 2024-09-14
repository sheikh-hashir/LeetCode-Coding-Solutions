# Intuition
- The problem asks us to calculate the percentage of customers whose first order was delivered on their preferred delivery date.
- To solve this, we need to first identify the earliest order date for each customer and then check if that order was delivered on their preferred delivery date.
<!-- Describe your first thoughts on how to solve this problem. -->

# Approach
- **Identify the Earliest Order:**
  - Use a subquery to find the minimum `order_date` for each `customer_id`.
- **Check for Preferred Delivery Date:**
  - Join the original table with the subquery to focus on the earliest orders.
  - Use a conditional statement to count the customers whose earliest order was delivered on their preferred delivery date.
- **Calculate the Percentage:**
  - Divide the count of such customers by the total number of customers and multiply by 100.
  - Use the `ROUND` function to format the result to two decimal places.
<!-- Describe your approach to solving the problem. -->


# Code
```
SELECT
    ROUND(
        (COUNT(DISTINCT CASE WHEN t.min_order_date = d.customer_pref_delivery_date THEN t.customer_id END) / COUNT(DISTINCT t.customer_id)) * 100, 2
    ) AS immediate_percentage
FROM
    (SELECT
         customer_id,
         MIN(order_date) AS min_order_date
     FROM
         delivery
     GROUP BY
         customer_id) t
JOIN
    delivery d
ON
    t.customer_id = d.customer_id
    AND t.min_order_date = d.order_date;

```