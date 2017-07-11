import media
import fresh_tomatoes


# Create instance of class Movie for each movie

# "Usual Suspects" movie details
toy_story = media.Movie(
    "Toy Story",
    "A cowboy doll is profoundly threatened and jealous when a new spaceman "
    "figure supplants him as top toy in a boy's room.",
    "img/toystory.jpg",
    "https://www.youtube.com/watch?v=4KPTXpQehio",
    "G",
    "http://www.imdb.com/title/tt0114709/?ref_=fn_al_tt_1"
    )

# "Usual Suspects" movie details
dumb_and_dumber = media.Movie(
    "Dumb and Dumber",
    "The cross-country adventures of two good-hearted but incredibly stupid "
    "friends.",
    "img/dumb.jpg",
    "https://www.youtube.com/watch?v=l13yPhimE3o",
    "PG-13",
    "http://www.imdb.com/title/tt0109686/?ref_=nv_sr_1"
    )

# "Usual Suspects" movie details
star_wars_iv = media.Movie(
    "Star Wars: A New Hope",
    "Luke Skywalker joins forces with a Jedi Knight, a cocky pilot, a "
    "wookiee and two droids to save the galaxy from the Empire's "
    "world-destroying battle-station, while also attempting to rescue "
    "Princess Leia from the evil Darth Vader.",
    "img/starwars.jpg",
    "https://www.youtube.com/watch?v=1g3_CFmnU7k",
    "PG",
    "http://www.imdb.com/title/tt0076759/?ref_=nv_sr_4"
    )

# "Usual Suspects" movie details
pulp_fiction = media.Movie(
    "Pulp Fiction",
    "The lives of two mob hit men, a boxer, a gangster's wife, and a pair "
    "of diner bandits intertwine in four tales of violence and redemption.",
    "img/pulp.jpg",
    "https://www.youtube.com/watch?v=s7EdQ4FqbhY",
    "R",
    "http://www.imdb.com/title/tt0110912/?ref_=nv_sr_1"
    )

# "Usual Suspects" movie details
fight_club = media.Movie(
    "Fight Club",
    "An insomniac office worker, looking for a way to change his life, "
    "crosses paths with a devil-may-care soap maker, forming an underground "
    "fight club that evolves into something much, much more.",
    "img/fight.jpg",
    "https://www.youtube.com/watch?v=BdJKm16Co6M",
    "R",
    "http://www.imdb.com/title/tt0137523/?ref_=nv_sr_1"
    )

# "Usual Suspects" movie details
forrest_gump = media.Movie(
    "Forrest Gump",
    "While not intelligent, Forrest Gump has accidentally been present at "
    "many historic moments, but his true love, Jenny Curran, eludes him.",
    "img/gump.jpg",
    "https://www.youtube.com/watch?v=bLvqoHBptjg",
    "PG-13",
    "http://www.imdb.com/title/tt0109830/?ref_=nv_sr_1"
    )

# "Usual Suspects" movie details
inception = media.Movie(
    "Inception",
    "A thief, who steals corporate secrets through use of dream-sharing "
    "technology, is given the inverse task of planting an idea into the "
    "mind of a CEO.",
    "img/inception.jpg",
    "https://www.youtube.com/watch?v=8hP9D6kZseM",
    "PG-13",
    "http://www.imdb.com/title/tt1375666/?ref_=nv_sr_1"
    )

# "The Matrix" movie details
matrix = media.Movie(
    "The Matrix",
    "A computer hacker learns from mysterious rebels about the true nature "
    "of his reality and his role in the war against its controllers.",
    "img/matrix.jpg",
    "https://www.youtube.com/watch?v=vKQi3bBA1y8",
    "R",
    "http://www.imdb.com/title/tt0133093/?ref_=nv_sr_1"
    )

# "Usual Suspects" movie details
usual_suspects = media.Movie(
    "The Usual Suspects",
    "A sole survivor tells of the twisty events leading up to a horrific "
    "gun battle on a boat, which began when five criminals met at a "
    "seemingly random police lineup.",
    "img/usual.jpg",
    "https://www.youtube.com/watch?v=oiXdPolca5w",
    "R",
    "http://www.imdb.com/title/tt0114814/?ref_=nv_sr_1"
    )

# Create list of movies
movies_list = [
    toy_story,
    dumb_and_dumber,
    star_wars_iv,
    pulp_fiction,
    fight_club,
    forrest_gump,
    inception,
    matrix,
    usual_suspects
    ]

# Open page in browser
fresh_tomatoes.open_movies_page(movies_list)
