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
