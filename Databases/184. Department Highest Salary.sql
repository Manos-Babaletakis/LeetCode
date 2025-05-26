-- Write your MySQL query statement below
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

-- solution 2
WITH ranked_salaries AS(
    SELECT 
        salary,
        name,
        departmentId,
        DENSE_RANK() OVER(PARTITION BY departmentId ORDER BY salary DESC) AS salary_rank
    FROM Employee  
)

SELECT
    d.name AS Department,
    r.name AS Employee,
    r.salary AS Salary
FROM
    ranked_salaries r
JOIN
    Department d
ON
    d.id = r.departmentId
WHERE r.salary_rank = 1;