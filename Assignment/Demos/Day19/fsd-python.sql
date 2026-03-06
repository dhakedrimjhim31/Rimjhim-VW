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
