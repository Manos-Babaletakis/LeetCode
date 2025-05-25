-- # Write your MySQL query statement below
Select C.name Customers
From Customers C
WHERE C.id NOT IN (SELECT DISTINCT(customerId)
                   FROM Orders);