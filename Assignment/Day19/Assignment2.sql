#Create Database:
CREATE DATABASE retail_company;
USE retail_company;

#Create Tables:
#Customers
CREATE TABLE Customers(
customer_id INT PRIMARY KEY,
name VARCHAR(50),
city VARCHAR(50)
);

#Products
CREATE TABLE Products(
product_id INT PRIMARY KEY,
product_name VARCHAR(50),
price INT
);

#Orders
CREATE TABLE Orders(
order_id INT PRIMARY KEY,
customer_id INT,
order_date DATE,
total_amount INT,
FOREIGN KEY (customer_id) REFERENCES Customers(customer_id)
);

#Order_Items
CREATE TABLE Order_Items(
order_item_id INT PRIMARY KEY,
order_id INT,
product_id INT,
quantity INT,
FOREIGN KEY (order_id) REFERENCES Orders(order_id),
FOREIGN KEY (product_id) REFERENCES Products(product_id)
);

#Insert Values:
#Customers
INSERT INTO Customers VALUES
(1,'Amit','Delhi'),
(2,'Priya','Mumbai'),
(3,'Rahul','Jaipur'),
(4,'Neha','Delhi'),
(5,'Rohan','Pune'),
(6,'Karan','Chennai'),
(7,'Anita','Kolkata'),
(8,'Vikas','Hyderabad'),
(9,'Sneha','Bangalore'),
(10,'Arjun','Ahmedabad');

#Products
INSERT INTO Products VALUES
(101,'Laptop',60000),
(102,'Mobile',30000),
(103,'Headphones',2000),
(104,'Keyboard',1500),
(105,'Mouse',800),
(106,'Monitor',12000),
(107,'Printer',9000),
(108,'Tablet',25000),
(109,'Speaker',3000),
(110,'Camera',45000);

#Orders
INSERT INTO Orders VALUES
(201,1,'2024-01-05',62000),
(202,2,'2024-01-10',30000),
(203,3,'2024-02-02',1500),
(204,1,'2024-02-15',12000),
(205,4,'2024-03-01',2000),
(206,5,'2024-03-10',800),
(207,1,'2024-03-15',9000),
(208,2,'2024-04-05',25000),
(209,3,'2024-04-20',3000),
(210,1,'2024-05-01',45000);

#Order_Items
INSERT INTO Order_Items VALUES
(1,201,101,1),
(2,202,102,1),
(3,203,104,1),
(4,204,106,1),
(5,205,103,1),
(6,206,105,1),
(7,207,107,1),
(8,208,108,1),
(9,209,109,1),
(10,210,110,1);

Query1: Customers who placed more than 3 orders
SELECT customer_id, COUNT(order_id) AS total_orders
FROM Orders
GROUP BY customer_id
HAVING COUNT(order_id) > 3;

#Query2:Total 5 customers by total spending
SELECT customer_id, SUM(total_amount) AS total_spending
FROM Orders
GROUP BY customer_id
ORDER BY total_spending DESC
LIMIT 5;

#Query3:Most ordered product
SELECT product_id, SUM(quantity) AS total_quantity
FROM Order_Items
GROUP BY product_id
ORDER BY total_quantity DESC
LIMIT 1;

#Query4:Customers who never placed an order
SELECT name
FROM Customers
WHERE customer_id NOT IN
(SELECT customer_id FROM Orders);

#Query5:Total revenue generated each month
SELECT MONTH(order_date) AS month,
SUM(total_amount) AS total_revenue
FROM Orders
GROUP BY MONTH(order_date);
