create database if not exists proj;
use proj;

drop table has,hasaccessto,supplies,emp,logins,supplier,product,customer,bill,dependents,dept,adminbill;

create table dept(did int(5) primary key,dname varchar(30));
create table emp(eid int(5) primary key,did int(5),fname varchar(15),lname varchar(15),job varchar(50),sal int(6),ephno bigint(10),eaddr varchar(50),age int(2),joindate date,foreign key(did) references dept(did) on delete cascade);
create table logins(elid int(5) primary key,username varchar(15) unique,pwd varchar(20) not null);
create table supplier(sid int(5),sname varchar(20),sphno bigint(10),saddr varchar(50),semail varchar(30),spid int(5) primary key);
create table product(pid int(5) primary key,pname varchar(20),ptype varchar(20),qty int(4),costprice float(6),mrp float(6));
create table customer(cname varchar(20),cphno bigint(10) unique,gender varchar(1));
create table dependents(deid int(5) primary key,did int(5),dename varchar(20),degender varchar(1),deage int(2),foreign key(did) references dept(did) on delete cascade);
create table bill(item varchar(20),mrp float(6),qty float(6),mrpxqty float(7));

create table has(eid int(5),deid int(5),foreign key(eid) references emp(eid) on delete cascade,foreign key(deid) references dependents(deid) on delete cascade);
create table hasaccessto(eid int(5),elid int(5),adate date,foreign key(eid) references emp(eid) on delete cascade,foreign key(elid) references logins(elid) on delete cascade);
create table supplies(spid int(5),pid int(5),foreign key(spid) references supplier(spid),foreign key(pid) references product(pid) on delete cascade);
create table buys(noofpro int(3));
create table adminbill(cphno bigint(10),pay_meth varchar(10),paidamt float(7),feedback varchar(15));

desc dept;
desc emp;
desc logins;
desc supplier;
desc product;
desc customer;
desc bill;
desc dependents;

desc has;
desc hasaccessto;
desc supplies;
desc buys;
desc bill;


insert into dept values
(1111,'Supervision'),
(2222,'Stock Maintenance'),
(3333,'Billing'),
(4444,'Security'),
(5555,'Supermarket Maintenance');

insert into emp values
(101,1111,'Arvind','Kumar','Assistant Store Manager',15000,9548697812,'Kuvempunagar,Mysuru',35,'2020-09-16'),
(102,2222,'Diya','Kumar','Inventory Control Specialist',14500,4256894321,'Vijaynagar,Mysuru',24,'2020-08-14'),
(103,2222,'Chaya','S Rao','Stock Clerk',13600,8765497296,'Siddharthnagar,Mysuru',25,'2021-04-10'),
(104,2222,'Advaitha','C','Stock Clerk',13000,9611874258,'Lakshmipuram,Mysuru',45,'2021-01-01'),
(105,3333,'Varsha','K','Cashier',10000,9448023213,'JP Nagar,Mysuru',20,'2022-10-19'),
(106,3333,'Puja','A','Cashier',12000,6548523571,'Gokulam,Mysuru',38,'2022-01-15'),
(107,3333,'Medini','S','Bagger',9000,3571598526,'Siddharthnagar,Mysuru',35,'2021-06-14'),
(108,3333,'Rahul','B','Bagger',10000,8524569515,'JP Nagar,Mysuru',28,'2020-04-28'),
(109,4444,'Chatush','M','Loss Prevention Associate',13600,7539518526,'Vijaynagar,Mysuru',29,'2022-11-15'),
(110,5555,'Manish','A C','Custodian',12000,9876543215,'Gokulam,Mysuru',32,'2021-12-18'),
(111,5555,'Jack','Thomas','Custodian',10000,6549873215,'Kuvempunagar,Mysuru',39,'2020-12-30');

insert into logins values
(1245,'scott','tiger'),
(1697,'chatush','tech'),
(1256,'miller','tech'),
(1645,'john','cat'),
(1829,'jack','tiger123'),
(1234,'admin','csrdk');

insert into supplier values
(121,'Aditya',9535349752,'Indranagar,Banglore','aditya2@gmail.com',12451),
(122,'Anand',9611318462,'RK Nagar,Mysuru','anand34@gmail.com',16421),
(123,'Abhishek',9448023203,'Kuvempunagar,Mysuru','abhi123@gmail.com',19635),
(124,'Bhuvan',8861575765,'Arvindnagar,Mysuru','bhuvan04@gmail.com',14897),
(125,'Dhanush',9261479361,'RK nagar,Mysuru','dhanush03@nagar.com',13423);

insert into product values
(131,'Lakme Sunscreen','Beauty',10,500,540),
(132,'Sprite','Beverage',50,30,40),
(133,'Lays','Snacks',30,8,10),
(134,'Maggi Noodles','Instant Food',20,10,12),
(135,'Chicken','Meat',10,240,280),
(136,'Rice','Food Grains',20,450,470),
(137,'Tomato','Vegetables',10,20,25),
(138,'Hide N Seek','Biscuit',50,35,40),
(139,'French Fries','Frozen Food',10,180,200),
(140,'Dove','Shampoo',10,145,160),
(141,'Vim','Liquid Soap',10,40,55);

insert into dependents values
(151,1111,'Vaishnavi','F',25),
(152,4444,'Riya','F',20),
(153,2222,'Suman','M',22),
(154,5555,'Ravi Kumar','M',28),
(155,3333,'Pranav','M',30);

insert into has values
(101,152),
(102,154),
(103,151),
(104,155),
(105,153);

insert into hasaccessto values
(101,1697,'2022-04-16'),
(102,1645,'2022-05-19'),
(103,1245,'2022-09-25'),
(104,1829,'2022-01-08'),
(105,1234,'2022-11-26');

insert into supplies values
(12451,131),
(12451,132),
(16421,133),
(16421,134),
(19635,135),
(19635,136),
(14897,137),
(14897,138),
(13423,139),
(13423,140),
(13423,141);


alter table product modify pname varchar(40);
drop table buys;
update product set pname='Maggi' where pid=134;
update supplies set spid=14897 where pid=139;
select fname,lname,sal from emp where sal>13000;
commit;

select * from dept;
select * from emp;
select * from logins;
select * from supplier;
select * from product;
select * from customer;
select * from dependents;
select * from has;
select * from hasaccessto;
select * from supplies;


(select did from emp where did=1111) union (select did from dept where did=3333);
(select fname,did from emp) union (select dname,did from dept);

(select did from dept where did=3333) union all (select did from emp where did=1111);
(select dname,did from dept) union all (select fname,did from emp);

select distinct did from emp where did in (select did from dept);

select did,sum(sal) as 'salary' from emp group by did;
select did,count(*) from emp group by did order by count(*) desc;

select job,max(sal) from emp group by job having max(sal) >= 13000;
select job,avg(sal) from emp group by job having job!='Cashier';


select fname,lname,sal from emp where sal between 12000 and 14600;
select pname,qty,mrp from product where mrp between 100 and 1000;
select fname,lname,job,eid from emp where eid between 103 and 106;

select fname from emp where fname like '____';
select fname,lname from emp where fname like '%ya';
select fname,eaddr from emp where eaddr like '_u%';

select * from emp where sal=(select max(sal) from emp);

delete from dept where did=4444;
select * from emp;
delete from dependents where did=2222; 
select e.fname,e.lname from emp as e where e.did in (select e.did from dependents as d where e.did=d.did);

(select did from emp) union (select did from dept);
(select did from emp) union all (select did from dept);