SELECT MAX(num) AS num
FROM (SELECT num from Mynumbers group by  num having count(num) = 1) as numbers;