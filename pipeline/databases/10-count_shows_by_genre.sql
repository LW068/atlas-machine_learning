-- Lists all genres and the number of shows linked to each, sorted by the number of shows linked
SELECT tv_genres.name 'genre', COUNT(tv_show_genres.genre_id) 'number_of_shows'
FROM tv_genres
INNER JOIN tv_show_genres
    ON tv_genres.id = tv_show_genres.genre_id
GROUP BY tv_genres.name
ORDER BY COUNT(tv_show_genres.genre_id) DESC