-- # Write your MySQL query statement below
Select C.name Customers
From Customers C
WHERE C.id NOT IN (SELECT DISTINCT(customerId)
                   FROM Orders);

-- solution 2
Select C.name Customers
From Customers C
LEFT JOIN Orders O ON
C.id = O.customerId
WHERE O.customerId IS NULL;