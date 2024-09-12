# Intuition
- The task involves calculating running totals and averages for a 7-day window based on the `visited_on` date.
- The query should compute the sum and average of the amount for the current and the previous 6 days.
- Additionally, the result should exclude the first 6 days since a 7-day window is required to compute these values.


<!-- Describe your first thoughts on how to solve this problem. -->

# Approach
- **Aggregate Data by Day:**
  - Create a Common Table Expression (`CTE`) called `VirtualCustomer` to aggregate data by visited_on.
  - This step groups the data by each day and calculates the total amount for each day.
  - The SQL query for this part is:
  - ```sql
    WITH virtualcustomer AS (
    SELECT visited_on,
           SUM(amount) AS vc_amount
    FROM   customer
    GROUP  BY visited_on
    )

- **Compute Rolling Sum and Average:**
  - In the outer query, use window functions to calculate the rolling sum and average over a 7-day window.
  - Window functions operate on a specified range of rows (in this case, 6 preceding rows plus the current row).
  - The `SUM` function calculates the total amount over the current day and the previous 6 days. Similarly, the `AVG` function calculates the average amount over the same period.
  - The SQL query for this part is
  - ```sql
    SELECT visited_on,
       SUM(vc_amount) OVER (ORDER BY visited_on ROWS BETWEEN 6 PRECEDING AND CURRENT ROW) AS amount,
       ROUND(AVG(vc_amount) OVER (ORDER BY visited_on ROWS BETWEEN 6 PRECEDING AND CURRENT ROW), 2) AS average_amount
    FROM   virtualcustomer

- **Assign Row Numbers:**
  - Use the `ROW_NUMBER()` window function to assign a sequential number to each row based on `visited_on`.
  - This helps in filtering out the first 6 rows where a complete 7-day window cannot be computed.
  - The SQL query for this part is
  - ```sql 
    SELECT visited_on,
       SUM(vc_amount) OVER (ORDER BY visited_on ROWS BETWEEN 6 PRECEDING AND CURRENT ROW) AS amount,
       ROUND(AVG(vc_amount) OVER (ORDER BY visited_on ROWS BETWEEN 6 PRECEDING AND CURRENT ROW), 2) AS average_amount,
       ROW_NUMBER() OVER (ORDER BY visited_on) AS rn
    FROM   virtualcustomer

- **Filter Out the First 6 Rows:**
  - In the final result, filter out rows where the row number (`rn`) is less than or equal to 6. 
  - This ensures that only rows with a full 7-day window (i.e., `rn > 6`) are included in the output.
  - The SQL query for this part is
  - ```sql
    SELECT visited_on,
       amount,
       average_amount
    FROM   (SELECT visited_on,
               SUM(vc_amount) OVER (ORDER BY visited_on ROWS BETWEEN 6 PRECEDING AND CURRENT ROW) AS amount,
               ROUND(AVG(vc_amount) OVER (ORDER BY visited_on ROWS BETWEEN 6 PRECEDING AND CURRENT ROW), 2) AS average_amount,
               ROW_NUMBER() OVER (ORDER BY visited_on) AS rn
        FROM   virtualcustomer) AS t
    WHERE  rn > 6
    ORDER  BY visited_on;
<!-- Describe your approach to solving the problem. -->

# Code
```mysql []
WITH VirtualCustomer
     AS (SELECT visited_on,
                SUM(amount) AS vc_amount
         FROM   customer
         GROUP  BY visited_on)
SELECT visited_on,
       amount,
       average_amount
FROM   (SELECT visited_on,
               SUM(vc_amount) OVER (ORDER BY visited_on ROWS BETWEEN 6 preceding AND CURRENT ROW) AS amount,
               Round(Avg(vc_amount) OVER (ORDER BY visited_on ROWS BETWEEN 6 preceding AND CURRENT ROW), 2) AS average_amount,
               ROW_NUMBER() OVER (ORDER BY visited_on) AS rn
        FROM   virtualcustomer) AS t
WHERE  rn > 6
ORDER  BY visited_on;
```
