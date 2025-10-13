-- Write your PostgreSQL query statement below
select w.id
from Weather as w   
join Weather as e
on  w.recordDate = e.recordDate + INTERVAL '1 day'
where w.temperature > e.temperature ;