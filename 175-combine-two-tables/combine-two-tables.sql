-- Write your PostgreSQL query statement below

-- s f j w g h o l

SELECT
    p.firstName,
    p.lastName,
    a.city,
    a.state
FROM Person p
LEFT JOIN Address a
    ON a.personId = p.personId;
