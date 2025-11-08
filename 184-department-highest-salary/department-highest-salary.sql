select 
  d.name as Department, 
  e.name as Employee, 
  e.salary as Salary 
from 
  Employee as e 
  join Department as d on e.departmentId = d.id 
where 
  (e.departmentID, e.salary) in (
    select 
      departmentId, 
      MAX(salary) 
    from 
      Employee 
    group by 
      departmentID
  )
