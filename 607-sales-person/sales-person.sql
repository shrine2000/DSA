-- Write your PostgreSQL query statement below

 

select sp.name
from SalesPerson as sp
where sp.sales_id not in (
    select os.sales_id 
    from Orders as os
    join Company as cp
    on os.com_id = cp.com_id
    where cp.name in ('RED')
)


