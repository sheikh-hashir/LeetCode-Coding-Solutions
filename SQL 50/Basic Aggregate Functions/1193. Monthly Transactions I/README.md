# Intuition
- When analyzing transactional data, it's important to gain insights on how different countries perform over time, especially regarding the total transaction counts, approval rates, and the monetary value of those transactions.
- Grouping transactions by country and month can help us better understand patterns and trends in the data.
<!-- Describe your first thoughts on how to solve this problem. -->

# Approach
- **Date Extraction:**
  - The `LEFT(trans_date, 7)` function is used to extract the year and month from the transaction date, allowing us to group the data on a monthly basis.
- **Grouping and Counting:**
  - We group the data by country and month to aggregate the number of transactions and the total amount of transactions.
- **Conditional Summing:**
  - The `SUM(CASE WHEN state = "approved" THEN amount ELSE 0 END)` is used to calculate the total amount for transactions that were approved.
- **Sorting:**
  - The final result is ordered by country and month to present the data in a structured and readable manner.
<!-- Describe your approach to solving the problem. -->

# Code
```
SELECT
    LEFT(trans_date, 7) AS month,
    country,
    COUNT(*) AS trans_count,
    SUM(state = "approved") AS approved_count,
    SUM(amount) AS trans_total_amount,
    SUM(CASE WHEN state = "approved" THEN amount ELSE 0 END) AS approved_total_amount
FROM
    Transactions
GROUP BY
    country,
    LEFT(trans_date, 7)
ORDER BY
    country,
    LEFT(trans_date, 7);

```