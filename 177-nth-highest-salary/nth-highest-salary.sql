CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  RETURN (
      SELECT DISTINCT Salary
      FROM (
          SELECT
              Salary,
              DENSE_RANK() OVER (ORDER BY Salary DESC) AS rnk
          FROM Employee
      ) AS ranked_salaries
      WHERE rnk = N
  );
END