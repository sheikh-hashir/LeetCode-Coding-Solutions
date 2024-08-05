# Intuition
- To find customers who have visited but have not made any transactions, we can leverage the `LEFT JOIN` operation.
- By joining the `Visits` table with the `Transactions` table on `visit_id` and filtering for `NULL` values in the `Transactions` table, we can identify visits without corresponding transactions.
<!-- Describe your first thoughts on how to solve this problem. -->

# Approach
- **LEFT JOIN:**
  - Use a `LEFT JOIN` to join the `Visits` table with the `Transactions` table based on the `visit_id`.
- **Filter:**
  - Filter the results where the `visit_id` in the `Transactions` table is `NULL`, indicating no transactions were made during the visit.
- **Grouping:**
  - Group the results by `customer_id` to get the count of such visits per customer.
<!-- Describe your approach to solving the problem. -->

# Code
```
# Write your MySQL query statement below
SELECT customer_id, count(v.customer_id) as count_no_trans FROM Visits v LEFT JOIN Transactions t ON v.visit_id =  t.visit_id WHERE t.visit_id IS NULL GROUP BY v.customer_id;

```