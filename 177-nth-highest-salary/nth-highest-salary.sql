CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
#Ek local variable 'M' bana rahe hain, bas ek number store karne ke liye.
  DECLARE M INT;
  
 # N-1 ki value 'M' me daal rahe hain, taki OFFSET ko direct number mile.
  SET M = N - 1;
  
  RETURN (
    SELECT DISTINCT Salary
    FROM Employee
   #Salaries ko bade se chhote order me lagana hai
    ORDER BY Salary DESC
   #Ab M salaries ko chhod kar, bas ek salary lena hai.
    LIMIT 1 OFFSET M
  );
END