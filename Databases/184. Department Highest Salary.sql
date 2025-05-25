# Write your MySQL query statement below
SELECT D.name   AS Department,
       E.name   AS Employee,
       E.salary AS Salary
FROM Employee E
INNER JOIN Department D
ON E.departmentId = D.id
WHERE (D.id, E.salary) IN 
    (SELECT departmentId, max(salary)
     FROM Employee
     GROUP BY departmentId);
