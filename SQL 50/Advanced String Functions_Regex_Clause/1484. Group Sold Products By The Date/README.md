# Intuition
- To analyze the sales activity for each day, we want to find out how many unique products were sold and list those products for each `sell_date`.
- By grouping the results by `sell_date`, we can summarize the number of distinct products sold on that day and display the list of products in a readable format.
<!-- Describe your first thoughts on how to solve this problem. -->

# Approach
- **Group by `sell_date`:**
  - We need to group all records by the `sell_date` to get per-day results.
- **Count distinct products:**
  - Use `COUNT(DISTINCT a.product)` to count how many unique products were sold on each `sell_date`.
- **Concatenate product names:**
  - Use `GROUP_CONCAT(DISTINCT a.product)` to concatenate the distinct products sold on that day into a single string, separated by commas.
- **Order the results:**
  - Sort the results by `sell_date` so that the sales records are presented in chronological order.
<!-- Describe your approach to solving the problem. -->

# Code
```mysql []
SELECT a.sell_date,
       Count(DISTINCT a.product)        AS num_sold,
       Group_concat(DISTINCT a.product) AS products
FROM   activities a
GROUP  BY a.sell_date
ORDER  BY a.sell_date;
```