INSERT INTO orders (order_id, customer_id, product_id, quantity, order_date, status)
VALUES
  (1, 101, 2001, 10, '2023-08-10', 'Processing'),
  (2, 102, 2002, 3, '2023-08-11', 'Shipped'),
  (3, 103, 2003, 2, '2023-08-12', 'Delivered'),
  (4, 101, 2004, 20, '2023-08-13', 'Processing'),
  (5, 104, 2001, 4, '2023-08-14', 'Shipped'),
  (6, 102, 2003, 2, '2023-08-15', 'Processing'),
  (7, 105, 2002, 3, '2023-08-16', 'Delivered'),
  (8, 101, 2005, 2, '2023-08-17', 'Shipped'),
  (9, 103, 2004, 30, '2023-08-18', 'Processing'),
  (10, 105, 2003, 3, '2023-08-19', 'Delivered');

  -- # connection.commit()