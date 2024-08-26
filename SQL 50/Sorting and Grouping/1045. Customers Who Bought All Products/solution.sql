SELECT customer_id
FROM   customer
GROUP  BY customer_id
HAVING (Count(DISTINCT product_key) = (SELECT Count(product_key) FROM product))