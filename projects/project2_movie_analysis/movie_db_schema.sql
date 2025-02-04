-- Create the database (if not using SQLite)
CREATE DATABASE movie_db;
USE movie_db;

-- Create Movies table
CREATE TABLE movies (
    movie_id SERIAL PRIMARY KEY,
    title VARCHAR(100) NOT NULL,
    release_year INT CHECK (release_year > 1900),
    genre VARCHAR(50),
    rating DECIMAL(2,1) CHECK (rating BETWEEN 0 AND 10)
);

-- Create Actors table
CREATE TABLE actors (
    actor_id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    birth_year INT CHECK (birth_year > 1900)
);

-- Create Movie_Actors table (Many-to-Many relationship)
CREATE TABLE movie_actors (
    movie_id INT,
    actor_id INT,
    role VARCHAR(100),
    PRIMARY KEY (movie_id, actor_id),
    FOREIGN KEY (movie_id) REFERENCES movies(movie_id) ON DELETE CASCADE,
    FOREIGN KEY (actor_id) REFERENCES actors(actor_id) ON DELETE CASCADE
);
