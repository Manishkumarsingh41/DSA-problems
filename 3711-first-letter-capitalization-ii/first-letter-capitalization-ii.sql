# Write your MySQL query statement below
WITH RECURSIVE w AS (
    SELECT content_id, content_text, REPLACE(content_text, '-', ' - ') t, 1 n,
           LENGTH(REPLACE(content_text, '-', ' - ')) - LENGTH(REPLACE(REPLACE(content_text, '-', ' - '), ' ', '')) + 1 c
    FROM user_content
    UNION ALL
    SELECT content_id, content_text, t, n + 1, c FROM w WHERE n < c
)
SELECT content_id, content_text original_text,
       REPLACE(GROUP_CONCAT(IF(SUBSTRING_INDEX(SUBSTRING_INDEX(t, ' ', n), ' ', -1) = '-', '-',
               CONCAT(UPPER(LEFT(SUBSTRING_INDEX(SUBSTRING_INDEX(t, ' ', n), ' ', -1), 1)),
                      LOWER(SUBSTRING(SUBSTRING_INDEX(SUBSTRING_INDEX(t, ' ', n), ' ', -1), 2))))
               ORDER BY n SEPARATOR ' '), ' - ', '-') converted_text
FROM w GROUP BY content_id, content_text ORDER BY content_id;