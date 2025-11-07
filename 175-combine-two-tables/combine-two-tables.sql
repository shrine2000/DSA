-- Write your PostgreSQL query statement below

-- s f j w g h o l

select p.firstName, p.lastName, a.city, a.state
from Person as p
left join Address a
on p.personId = a.personId;
