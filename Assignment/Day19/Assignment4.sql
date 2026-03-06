CREATE DATABASE ecommerce_analysis;
USE ecommerce_analysis;

CREATE TABLE Orders(
order_id INT PRIMARY KEY,
customer_id INT,
product_id INT,
quantity INT,
total_amount INT
);

INSERT INTO Orders VALUES
(1,101,201,20,5000),
(2,102,202,15,3000),
(3,101,203,25,7000),
(4,103,201,30,6000),
(5,104,204,10,2000),
(6,101,202,40,8000),
(7,102,205,35,9000),
(8,105,203,50,10000),
(9,103,204,15,4000),
(10,106,201,60,12000),
(11,101,205,18,6500),
(12,102,202,45,9500),
(13,107,203,30,7000),
(14,108,204,20,5000),
(15,105,205,55,11000),
(16,103,201,35,7500),
(17,102,202,50,12000),
(18,101,203,40,8500),
(19,109,204,25,4500),
(20,110,205,70,14000);

SELECT customer_id, SUM(total_amount) AS total_spent
FROM Orders
GROUP BY customer_id;

SELECT customer_id, COUNT(order_id) AS total_orders
FROM Orders
GROUP BY customer_id;

SELECT customer_id, COUNT(order_id) AS total_orders
FROM Orders
GROUP BY customer_id
HAVING COUNT(order_id) > 3;

SELECT customer_id, SUM(total_amount) AS total_spent
FROM Orders
GROUP BY customer_id
HAVING SUM(total_amount) > 10000;

SELECT product_id, SUM(quantity) AS total_quantity
FROM Orders
GROUP BY product_id
HAVING SUM(quantity) > 100;
