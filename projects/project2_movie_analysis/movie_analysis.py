import sqlite3

# Connect to the SQLite database (or create if it doesn't exist)
conn = sqlite3.connect("movie_db.sqlite")
cursor = conn.cursor()

# Create tables
cursor.executescript("""
    CREATE TABLE IF NOT EXISTS movies (
        movie_id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        release_year INTEGER CHECK (release_year > 1900),
        genre TEXT,
        rating REAL CHECK (rating BETWEEN 0 AND 10)
    );

    CREATE TABLE IF NOT EXISTS actors (
        actor_id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        birth_year INTEGER CHECK (birth_year > 1900)
    );

    CREATE TABLE IF NOT EXISTS movie_actors (
        movie_id INTEGER,
        actor_id INTEGER,
        role TEXT,
        PRIMARY KEY (movie_id, actor_id),
        FOREIGN KEY (movie_id) REFERENCES movies(movie_id) ON DELETE CASCADE,
        FOREIGN KEY (actor_id) REFERENCES actors(actor_id) ON DELETE CASCADE
    );
""")

# Insert sample data
cursor.executemany("INSERT INTO movies (title, release_year, genre, rating) VALUES (?, ?, ?, ?)", 
                   [("Inception", 2010, "Sci-Fi", 8.8),
                    ("The Dark Knight", 2008, "Action", 9.0),
                    ("Interstellar", 2014, "Sci-Fi", 8.6),
                    ("Titanic", 1997, "Romance", 7.8),
                    ("Avatar", 2009, "Sci-Fi", 7.9)])

cursor.executemany("INSERT INTO actors (name, birth_year) VALUES (?, ?)", 
                   [("Leonardo DiCaprio", 1974),
                    ("Christian Bale", 1974),
                    ("Matthew McConaughey", 1969),
                    ("Kate Winslet", 1975),
                    ("Morgan Freeman", 1937)])

cursor.executemany("INSERT INTO movie_actors (movie_id, actor_id, role) VALUES (?, ?, ?)", 
                   [(1, 1, "Dom Cobb"),  # Leonardo in Inception
                    (2, 2, "Bruce Wayne"),  # Christian Bale in The Dark Knight
                    (3, 3, "Cooper"),  # Matthew McConaughey in Interstellar
                    (4, 1, "Jack Dawson"),  # Leonardo in Titanic
                    (4, 4, "Rose DeWitt Bukater")])  # Kate Winslet in Titanic

conn.commit()

# Fetch and display top-rated movies
cursor.execute("SELECT title, rating FROM movies WHERE rating > 8.5")
top_movies = cursor.fetchall()

print("Top Rated Movies (Above 8.5):")
for title, rating in top_movies:
    print(f"{title}: {rating}")

# Fetch and display actors in Titanic
cursor.execute("""
    SELECT actors.name, movie_actors.role 
    FROM actors
    JOIN movie_actors ON actors.actor_id = movie_actors.actor_id
    JOIN movies ON movie_actors.movie_id = movies.movie_id
    WHERE movies.title = 'Titanic'
""")
titanic_cast = cursor.fetchall()

print("\nActors in Titanic:")
for name, role in titanic_cast:
    print(f"{name} as {role}")

# Close the connection
conn.close()
