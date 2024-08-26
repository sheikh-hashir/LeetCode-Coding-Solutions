# Intuition
- To find customers who have purchased all available products, you need to count the number of distinct products each customer has purchased and compare it with the total number of products available in the `product` table.
- If the counts match, that customer has purchased all products.
<!-- Describe your first thoughts on how to solve this problem. -->

# Approach
- Group the `Customer` table by `customer_id`.
- Count the distinct `product_key` for each `customer_id`.
- Compare the distinct product count for each customer with the total number of products available in the `product` table.
- Select only those customers where the counts match.
<!-- Describe your approach to solving the problem. -->

# Code
```mysql []
SELECT customer_id
FROM   customer
GROUP  BY customer_id
HAVING (Count(DISTINCT product_key) = (SELECT Count(product_key) FROM product))
```