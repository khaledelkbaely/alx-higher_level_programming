-- lists all genres from hbtn_0d_tvshows
-- diplays the number of shows linked to it
SELECT tvg.name AS genre, COUNT(tvsg.genre_id) AS number_of_shows
FROM tv_genres AS tvg
INNER JOIN tv_show_genres AS tvsg
ON tvg.id = tvsg.genre_id
GROUP BY tvsg.genre_id
ORDER BY number_of_shows DESC;
