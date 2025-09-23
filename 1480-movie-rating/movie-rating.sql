(SELECT name AS results
 FROM Users u
 JOIN MovieRating r ON u.user_id = r.user_id
 GROUP BY u.user_id, u.name
 ORDER BY COUNT(*) DESC, name
 LIMIT 1)
UNION ALL
(SELECT title AS results
 FROM Movies m
 JOIN MovieRating r ON m.movie_id = r.movie_id
 WHERE r.created_at >= '2020-02-01' AND r.created_at <= '2020-02-29'
 GROUP BY m.movie_id, m.title
 ORDER BY AVG(r.rating) DESC, title
 LIMIT 1);
