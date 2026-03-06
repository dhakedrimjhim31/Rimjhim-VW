create database fsd;
 
show databases;
 
use fsd;
 
create table employees(emp_id int primary key,emp_name varchar(30),salary float);
show tables;
 
desc employees;
 
insert into employees values(1,'rahul',45000);
 
select * from employees;
 
insert into employees(emp_id,emp_name,salary)
values(2,'rahul',45000);
 
insert into employees(emp_id,emp_name)values(3,'pooja');
select emp_name,salary from employees;
 
alter table employees
change emp_id emp_id int auto_increment;
 
desc employees;



insert into employees(emp_name,salary)
values('amit',34000.78);
 
select 5/10 as "result";
select 5>=5;
 
use ai;
show tables;
 
select * from employees;
 
#fetch employees whose salary greater than 50,000 and city is bangalore
select * from
employees
where emp_salary>70000
or emp_city='bangalore';
 
select *
from employees

where emp_salary between 50000 and 60000;

select * from employees
where emp_city in('bangalore','mumbai','kanpur');
 
select * from employees
where emp_name like '_r%';
 
select * from employees
where email is null;
select * from employees;
 
update employees
set emp_salary=30000
where emp_id=7;
 
select * from employees;
 
delete from employees
where emp_id=4;

###
alter table employees
drop column dept;

alter table employees
change salary emp_salary int;


select sum(duration),subject_name
from tutorials
group by subject_name
having sum(duration)>20;

#########
•SELECT column-names
  FROM table-name
  WHERE condition
  GROUP BY column-names
  HAVING condition
 
•SELECT column-names
  FROM table-name
  WHERE condition
  GROUP BY column-names
  HAVING condition
  ORDER BY column-names

########
Select column-list
  fromtable_name
  where condition
  [group by column]
  [order by column];



####
select sum(duration),subject_name
from tutorials
where subject_name<>'python'
group by subject_name
having sum(duration)>20;

#######
create table customers(id int primary key auto_increment,cust_name varchar(30),cust_city varchar(30));
 
create table orders(id int primary key auto_increment,
ord_name varchar(30),
ord_price int,
ord_qty int,
cust_id int,
foreign key(cust_id)references customers(id));
 
insert into customers(cust_name,cust_city)
values('ravi','mumbai'),
('amit','lucknow'),
('priya','mumbai'),
('alok','agra')
 
select * from customers;
 
insert into orders
(ord_name,ord_price,ord_qty,cust_id)
values('laptop',60000,1,2),('mobile cover',1000,2,3);

#########
select cust_name,ord_name,ord_qty
from customers
inner join orders
on customers.id=orders.cust_id;

select cust_name,ord_name,ord_qty
from customers,orders
where customers.id=orders.cust_id;
 
 
select cust_name,ord_name,ord_qty
from customers
left join orders
on customers.id=orders.cust_id;

select cust_name,ord_name,ord_qty
from customers
right join orders
on customers.id=orders.cust_id;

#####
select emp_name from employees where
emp_salary=(select max(emp_salary) from employees);
 

#####
select dept_name
from department,employees
where department.id=employees.emp_id
group by dept_name
having count(*)<2;



######### ASSIGNMENT 1:
CREATE DATABASE company;
USE company;

CREATE TABLE Employees (
emp_id INT PRIMARY KEY,
emp_name VARCHAR(50),
department VARCHAR(50),
salary INT,
joining_date DATE
);

CREATE TABLE Projects (
project_id INT PRIMARY KEY,
project_name VARCHAR(50),
start_date DATE,
end_date DATE
);

CREATE TABLE Employee_Project (
emp_id INT,
project_id INT,
hours_worked INT,
rating INT,
FOREIGN KEY (emp_id) REFERENCES Employees(emp_id),
FOREIGN KEY (project_id) REFERENCES Projects(project_id)
);

INSERT INTO Employees VALUES
(1,'Rahul','IT',60000,'2022-01-10'),
(2,'Priya','HR',50000,'2021-05-15'),
(3,'Amit','IT',70000,'2020-03-20'),
(4,'Neha','Finance',65000,'2022-08-01'),
(5,'Ravi','IT',55000,'2023-02-10');

INSERT INTO Projects VALUES
(101,'Website','2023-01-01','2023-03-01'),
(102,'Mobile App','2023-02-01','2023-05-01'),
(103,'Database','2023-04-01','2023-06-01');

INSERT INTO Employee_Project VALUES
(1,101,40,5),
(1,102,35,4),
(1,103,30,5),
(2,101,20,3),
(3,101,50,5),
(3,102,45,4),
(4,103,25,4);

SELECT emp_id
FROM Employee_Project
GROUP BY emp_id
HAVING COUNT(project_id) > 2;

SELECT emp_id, AVG(rating) AS avg_rating
FROM Employee_Project
GROUP BY emp_id
HAVING AVG(rating) > 4;

SELECT emp_name, department, salary
FROM Employees e
WHERE salary = (
SELECT MAX(salary)
FROM Employees
WHERE department = e.department
);

SELECT emp_name
FROM Employees
WHERE emp_id NOT IN
(SELECT emp_id FROM Employee_Project);

SELECT project_id, SUM(hours_worked) AS total_hours
FROM Employee_Project
GROUP BY project_id
ORDER BY total_hours DESC
LIMIT 1;




################ ASSIGNMENT2:
CREATE DATABASE retail_company;
USE retail_company;

CREATE TABLE Customers(
customer_id INT PRIMARY KEY,
name VARCHAR(50),
city VARCHAR(50)
);

CREATE TABLE Products(
product_id INT PRIMARY KEY,
product_name VARCHAR(50),
price INT
);

CREATE TABLE Orders(
order_id INT PRIMARY KEY,
customer_id INT,
order_date DATE,
total_amount INT,
FOREIGN KEY (customer_id) REFERENCES Customers(customer_id)
);

CREATE TABLE Order_Items(
order_item_id INT PRIMARY KEY,
order_id INT,
product_id INT,
quantity INT,
FOREIGN KEY (order_id) REFERENCES Orders(order_id),
FOREIGN KEY (product_id) REFERENCES Products(product_id)
);

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

SELECT customer_id, COUNT(order_id) AS total_orders
FROM Orders
GROUP BY customer_id
HAVING COUNT(order_id) > 3;

SELECT customer_id, SUM(total_amount) AS total_spending
FROM Orders
GROUP BY customer_id
ORDER BY total_spending DESC
LIMIT 5;

SELECT product_id, SUM(quantity) AS total_quantity
FROM Order_Items
GROUP BY product_id
ORDER BY total_quantity DESC
LIMIT 1;

SELECT name
FROM Customers
WHERE customer_id NOT IN
(SELECT customer_id FROM Orders);

SELECT MONTH(order_date) AS month,
SUM(total_amount) AS total_revenue
FROM Orders
GROUP BY MONTH(order_date);




#################### ASSIGNMENT 3:
CREATE DATABASE company_analysis;
USE company_analysis;

CREATE TABLE Employees (
emp_id INT PRIMARY KEY,
emp_name VARCHAR(50),
department VARCHAR(50),
salary INT
);

INSERT INTO Employees VALUES
(1,'Amit','IT',60000),
(2,'Priya','HR',50000),
(3,'Rahul','IT',75000),
(4,'Neha','Finance',65000),
(5,'Rohan','IT',55000),
(6,'Anita','HR',52000),
(7,'Vikas','Finance',70000),
(8,'Sneha','IT',80000),
(9,'Karan','HR',48000),
(10,'Arjun','Finance',72000);

SELECT emp_name, salary
FROM Employees
WHERE salary > (SELECT AVG(salary) FROM Employees);

SELECT emp_name, department, salary
FROM Employees e
WHERE salary > (
SELECT AVG(salary)
FROM Employees
WHERE department = e.department
);

SELECT emp_name, department, salary
FROM Employees e
WHERE salary = (
SELECT MAX(salary)
FROM Employees
WHERE department = e.department
);

SELECT emp_name, salary
FROM Employees
WHERE salary < (SELECT MAX(salary) FROM Employees)
AND salary > (SELECT AVG(salary) FROM Employees);

SELECT department, AVG(salary) AS avg_salary
FROM Employees
GROUP BY department
HAVING AVG(salary) > (SELECT AVG(salary) FROM Employees);



############## ASSIGNMENT 4:
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

