import media
import fresh_tomatoes


# Create instance of class Movie for each movie
toy_story = media.Movie("Toy Story",
                        "A cowboy doll is profoundly threatened and jealous when a new spaceman figure supplants him as top toy in a boy's room.",  # NOQA
                        "https://images-na.ssl-images-amazon.com/images/M/MV5BMDU2ZWJlMjktMTRhMy00ZTA5LWEzNDgtYmNmZTEwZTViZWJkXkEyXkFqcGdeQXVyNDQ2OTk4MzI@._V1_SY1000_SX670_AL_.jpg",  # NOQA
                        "https://www.youtube.com/watch?v=4KPTXpQehio",
                        "G",
                        "http://www.imdb.com/title/tt0114709/?ref_=fn_al_tt_1")

dumb_and_dumber = media.Movie("Dumb and Dumber",
                              "The cross-country adventures of two good-hearted but incredibly stupid friends.",  # NOQA
                              "https://images-na.ssl-images-amazon.com/images/M/MV5BZDQwMjNiMTQtY2UwYy00NjhiLTk0ZWEtZWM5ZWMzNGFjNTVkXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_.jpg",  # NOQA
                              "https://www.youtube.com/watch?v=l13yPhimE3o",
                              "PG-13",
                              "http://www.imdb.com/title/tt0109686/?ref_=nv_sr_1")  # NOQA

star_wars_iv = media.Movie("Star Wars: A New Hope",
                           "Luke Skywalker joins forces with a Jedi Knight, a cocky pilot, a wookiee and two droids to save the galaxy from the Empire's world-destroying battle-station, while also attempting to rescue Princess Leia from the evil Darth Vader.",  # NOQA
                           "https://images-na.ssl-images-amazon.com/images/M/MV5BYzQ2OTk4N2QtOGQwNy00MmI3LWEwNmEtOTk0OTY3NDk2MGJkL2ltYWdlL2ltYWdlXkEyXkFqcGdeQXVyNjc1NTYyMjg@._V1_SY1000_CR0,0,664,1000_AL_.jpg",  # NOQA
                           "https://www.youtube.com/watch?v=1g3_CFmnU7k",
                           "PG",
                           "http://www.imdb.com/title/tt0076759/?ref_=nv_sr_4")

pulp_fiction = media.Movie("Pulp Fiction",
                           "The lives of two mob hit men, a boxer, a gangster's wife, and a pair of diner bandits intertwine in four tales of violence and redemption.",  # NOQA
                           "https://images-na.ssl-images-amazon.com/images/M/MV5BMTkxMTA5OTAzMl5BMl5BanBnXkFtZTgwNjA5MDc3NjE@._V1_SY1000_CR0,0,673,1000_AL_.jpg",  # NOQA
                           "https://www.youtube.com/watch?v=s7EdQ4FqbhY",
                           "R",
                           "http://www.imdb.com/title/tt0110912/?ref_=nv_sr_1")

fight_club = media.Movie("Fight Club",
                         "An insomniac office worker, looking for a way to change his life, crosses paths with a devil-may-care soap maker, forming an underground fight club that evolves into something much, much more.",  # NOQA
                         "https://images-na.ssl-images-amazon.com/images/M/MV5BZGY5Y2RjMmItNDg5Yy00NjUwLThjMTEtNDc2OGUzNTBiYmM1XkEyXkFqcGdeQXVyNjU0OTQ0OTY@._V1_.jpg",  # NOQA
                         "https://www.youtube.com/watch?v=BdJKm16Co6M",
                         "R",
                         "http://www.imdb.com/title/tt0137523/?ref_=nv_sr_1")

forrest_gump = media.Movie("Forrest Gump",
                           "While not intelligent, Forrest Gump has accidentally been present at many historic moments, but his true love, Jenny Curran, eludes him.",  # NOQA
                           "https://images-na.ssl-images-amazon.com/images/M/MV5BYThjM2MwZGMtMzg3Ny00NGRkLWE4M2EtYTBiNWMzOTY0YTI4XkEyXkFqcGdeQXVyNDYyMDk5MTU@._V1_SY1000_CR0,0,757,1000_AL_.jpg",  # NOQA
                           "https://www.youtube.com/watch?v=bLvqoHBptjg",
                           "PG-13",
                           "http://www.imdb.com/title/tt0109830/?ref_=nv_sr_1")

inception = media.Movie("Inception",
                        "A thief, who steals corporate secrets through use of dream-sharing technology, is given the inverse task of planting an idea into the mind of a CEO.",  # NOQA
                        "https://images-na.ssl-images-amazon.com/images/M/MV5BMjAxMzY3NjcxNF5BMl5BanBnXkFtZTcwNTI5OTM0Mw@@._V1_SY1000_CR0,0,675,1000_AL_.jpg",  # NOQA
                        "https://www.youtube.com/watch?v=8hP9D6kZseM",
                        "PG-13",
                        "http://www.imdb.com/title/tt1375666/?ref_=nv_sr_1")

matrix = media.Movie("The Matrix",
                     "A computer hacker learns from mysterious rebels about the true nature of his reality and his role in the war against its controllers.",  # NOQA
                     "https://images-na.ssl-images-amazon.com/images/M/MV5BNzQzOTk3OTAtNDQ0Zi00ZTVkLWI0MTEtMDllZjNkYzNjNTc4L2ltYWdlXkEyXkFqcGdeQXVyNjU0OTQ0OTY@._V1_SY1000_CR0,0,665,1000_AL_.jpg",  # NOQA
                     "https://www.youtube.com/watch?v=vKQi3bBA1y8",
                     "R",
                     "http://www.imdb.com/title/tt0133093/?ref_=nv_sr_1")

usual_suspects = media.Movie("The Usual Suspects",
                             "A sole survivor tells of the twisty events leading up to a horrific gun battle on a boat, which began when five criminals met at a seemingly random police lineup.",  # NOQA
                             "https://images-na.ssl-images-amazon.com/images/M/MV5BYTViNjMyNmUtNDFkNC00ZDRlLThmMDUtZDU2YWE4NGI2ZjVmXkEyXkFqcGdeQXVyNjU0OTQ0OTY@._V1_SY1000_CR0,0,670,1000_AL_.jpg",  # NOQA
                             "https://www.youtube.com/watch?v=oiXdPolca5w",
                             "R",
                             "http://www.imdb.com/title/tt0114814/?ref_=nv_sr_1")  # NOQA

# Create list of movies
movies_list = [toy_story, dumb_and_dumber, star_wars_iv, pulp_fiction,
               fight_club, forrest_gump, inception, matrix, usual_suspects]

# Open page in browser
fresh_tomatoes.open_movies_page(movies_list)
