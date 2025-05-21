# Write your MySQL query statement below
SELECT DISTINCT(P1.email) AS Email
FROM Person P1 INNER JOIN
     Person P2 ON
     P1.email = P2.email
WHERE P1.id != P2.id;

#2nd way
SELECT email AS Email
FROM Person
group by email
having count(email) > 1;