SELECT a.sell_date,
       Count(DISTINCT a.product)        AS num_sold,
       Group_concat(DISTINCT a.product) AS products
FROM   activities a
GROUP  BY a.sell_date
ORDER  BY a.sell_date;