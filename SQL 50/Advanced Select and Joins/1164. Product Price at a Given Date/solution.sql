SELECT
    p.product_id,
    COALESCE(
        (SELECT new_price
         FROM Products
         WHERE change_date <= '2019-08-16'
         AND product_id = p.product_id
         ORDER BY change_date DESC
         LIMIT 1),
        10
    ) AS price
FROM
    Products p
GROUP BY
    p.product_id;