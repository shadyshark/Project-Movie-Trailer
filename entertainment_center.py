import fresh_tomatoes
# Link entertainment_center.py with media.py by importing media
import media
# Create multiple instances of Movie Class
firstdates = media.Movie(
    "50 First Dates",
    "Henry Roth is a veterinarian at Sea Life Park on the island of Oahu",
    "https://upload.wikimedia.org/wikipedia/en/9/9d/50FirstDates.jpg",
    "https://www.youtube.com/watch?v=H1SVxJZTgI4")

august_rush = media.Movie(
    "August Rush",
    "an 11-year-old musical prodigy living in an orphanage \
    who runs away to New York City",
    "https://upload.wikimedia.org/wikipedia/en/1/1b/August_rush_poster.jpg",
    "https://www.youtube.com/watch?v=nRGYeyS1jzw")

music_and_lyrics = media.Movie(
    "Music And lyrics",
    "Alex Fletcher (Hugh Grant) is a washed-up former pop star \
    who is attempting to revive his dwindling career \
    by hitching his name to the rising star of Cora Corman",
    "https://upload.wikimedia.org/wikipedia/en/d/d3/Music_and_lyrics.jpg",
    "https://www.youtube.com/watch?v=4C6sSZlVKZE")

camp_rock = media.Movie(
    "Camp_Rock_2",
    "Mitchie Torres returns to Camp Rock for another summer year,\
    along with her friends and her love",
    "https://upload.wikimedia.org/wikipedia/en/c/c8/CampRock2DVD.jpg",
    "https://www.youtube.com/watch?v=1yKLEoImqw8")

troy = media.Movie(
    "Troy",
    "In the late 12th Century BC, a battle between the armies of King \
    Agamemnon of Mycenae and Triopas of Thessaly is averted \
    when the great warrior",
    "https://upload.wikimedia.org/wikipedia/en/b/b8/Troy2004Poster.jpg",
    "https://www.youtube.com/watch?v=znTLzRJimeY")

dear_john = media.Movie(
    "Dear John",
    "It follows the life of a soldier (Channing Tatum) \
    after he falls in love with a young woman",
    "https://upload.wikimedia.org/wikipedia/en/3/35/Dear_John_film_poster.jpg",
    "https://www.youtube.com/watch?v=r0fq5dd0C60")
# Create alist of movies to generate the html file by using
# open_movies_page function in fresh_tomatoes module
movies = [
    firstdates,
    august_rush,
    music_and_lyrics,
    camp_rock,
    troy,
    dear_john]
fresh_tomatoes.open_movies_page(movies)
