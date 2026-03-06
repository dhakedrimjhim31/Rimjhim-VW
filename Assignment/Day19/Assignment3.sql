#Create Database:
CREATE DATABASE company_analysis;
USE company_analysis;

#Create Employees Table:
CREATE TABLE Employees (
emp_id INT PRIMARY KEY,
emp_name VARCHAR(50),
department VARCHAR(50),
salary INT
);

#Inserting Values:
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

#Query1:Employees whose salary is greater than the average salary of all employees
SELECT emp_name, salary
FROM Employees
WHERE salary > (SELECT AVG(salary) FROM Employees);

#Query2:Employees whose salary is greater than the average salary of their department
SELECT emp_name, department, salary
FROM Employees e
WHERE salary > (
SELECT AVG(salary)
FROM Employees
WHERE department = e.department
);

#Query3:Employees who earn the highest salary in their department
SELECT emp_name, department, salary
FROM Employees e
WHERE salary = (
SELECT MAX(salary)
FROM Employees
WHERE department = e.department
);

#Query4:Employees who earn less than the highest salary in the company but more than the average salary.
SELECT emp_name, salary
FROM Employees
WHERE salary < (SELECT MAX(salary) FROM Employees)
AND salary > (SELECT AVG(salary) FROM Employees);

#Query5:Departments whose average salary is greater than the company average salary.
SELECT department, AVG(salary) AS avg_salary
FROM Employees
GROUP BY department
HAVING AVG(salary) > (SELECT AVG(salary) FROM Employees);
