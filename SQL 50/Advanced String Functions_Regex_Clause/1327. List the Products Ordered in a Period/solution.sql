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