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

