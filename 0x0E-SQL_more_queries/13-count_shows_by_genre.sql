-- 13-count_shows_by_genre.sql

USE hbtn_0d_tvshows;

SELECT tv_show_genres.genre AS genre, COUNT(tv_shows.id) AS number_of_shows
FROM tv_shows
JOIN tv_show_genres ON tv_shows.id = tv_show_genres.tv_show_id
GROUP BY genre
ORDER BY number_of_shows DESC;
