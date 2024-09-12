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
