SELECT 
    request_at AS Day,             -- har din ka data
    ROUND(
        SUM(status != 'completed') / COUNT(*), 2
    ) AS "Cancellation Rate"       -- cancelled / total trips
FROM Trips t
JOIN Users c 
    ON t.client_id = c.users_id AND c.banned = 'No'   -- sirf un-clients jo banned nahi
JOIN Users d 
    ON t.driver_id = d.users_id AND d.banned = 'No'   -- sirf un-drivers jo banned nahi
WHERE request_at BETWEEN '2013-10-01' AND '2013-10-03' -- 1st to 3rd Oct data
GROUP BY request_at;              -- har din ka group
