-- Insert sample movies
INSERT INTO movies (title, release_year, genre, rating) VALUES
('Inception', 2010, 'Sci-Fi', 8.8),
('The Dark Knight', 2008, 'Action', 9.0),
('Interstellar', 2014, 'Sci-Fi', 8.6),
('Titanic', 1997, 'Romance', 7.8),
('Avatar', 2009, 'Sci-Fi', 7.9);

-- Insert sample actors
INSERT INTO actors (name, birth_year) VALUES
('Leonardo DiCaprio', 1974),
('Christian Bale', 1974),
('Matthew McConaughey', 1969),
('Kate Winslet', 1975),
('Morgan Freeman', 1937);

-- Insert movie-actor relationships
INSERT INTO movie_actors (movie_id, actor_id, role) VALUES
(1, 1, 'Dom Cobb'),  -- Leonardo in Inception
(2, 2, 'Bruce Wayne'),  -- Christian Bale in The Dark Knight
(3, 3, 'Cooper'),  -- Matthew McConaughey in Interstellar
(4, 1, 'Jack Dawson'),  -- Leonardo in Titanic
(4, 4, 'Rose DeWitt Bukater');  -- Kate Winslet in Titanic

-- Retrieve all Sci-Fi movies
SELECT title, release_year, rating FROM movies WHERE genre = 'Sci-Fi';

-- Find movies with rating above 8.5
SELECT title, rating FROM movies WHERE rating > 8.5;

-- Count movies per genre
SELECT genre, COUNT(*) AS movie_count FROM movies GROUP BY genre;

-- Find all actors in a specific movie
SELECT movies.title, actors.name, movie_actors.role 
FROM movies
JOIN movie_actors ON movies.movie_id = movie_actors.movie_id
JOIN actors ON movie_actors.actor_id = actors.actor_id
WHERE movies.title = 'Titanic';
