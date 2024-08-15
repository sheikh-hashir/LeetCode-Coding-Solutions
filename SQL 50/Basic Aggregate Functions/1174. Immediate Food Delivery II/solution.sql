SELECT
    ROUND(
        (COUNT(DISTINCT CASE WHEN t.min_order_date = d.customer_pref_delivery_date THEN t.customer_id END) / COUNT(DISTINCT t.customer_id)) * 100, 2
    ) AS immediate_percentage
FROM
    (SELECT
         customer_id,
         MIN(order_date) AS min_order_date
     FROM
         delivery
     GROUP BY
         customer_id) t
JOIN
    delivery d
ON
    t.customer_id = d.customer_id
    AND t.min_order_date = d.order_date;
