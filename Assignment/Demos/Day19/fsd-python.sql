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
