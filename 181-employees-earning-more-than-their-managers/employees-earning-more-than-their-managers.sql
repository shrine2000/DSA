-- Write your PostgreSQL query statement below

 select  e2.name AS Employee from Employee e1
 inner join Employee e2 on e1.id= e2.managerid
 where e2.salary > e1.salary;
 