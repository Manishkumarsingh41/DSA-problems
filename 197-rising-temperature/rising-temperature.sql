SELECT a.Id
FROM Weather a
JOIN Weather b
  ON DATEDIFF(a.recordDate, b.recordDate) = 1
WHERE a.Temperature > b.Temperature;
