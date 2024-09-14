SELECT p.product_name, s.year, s.price FROM Product p INNER JOIN Sales s on s.product_id = p.product_id
