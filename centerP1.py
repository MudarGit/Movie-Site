import fresh_tomatoes
#imports fresh_tomatoes.py to help generate the page out of our movies list.
import mediaP1
#imports mediaP1.py so the Movie class may be used.

matrix = mediaP1.Movie("The Matrix",
                        "A sci-fi story about a man trying to find meaning in his life.",
                        "https://upload.wikimedia.org/wikipedia/en/c/c1/The_Matrix_Poster.jpg",
                        "https://www.youtube.com/watch?v=m8e-FF8MsqU")
#creates the matrix instance of the class movie

signs = mediaP1.Movie("Signs",
                        "A movie of alien invasion",
                        "http://www.gstatic.com/tv/thumb/movieposters/30099/p30099_p_v8_ad.jpg",
                        "https://www.youtube.com/watch?v=F5-Lv4CJmFM")
#creates the signs instance of the class movie

fight_club = mediaP1.Movie("Fight Club",
                        "A movie about fights and stuff usually in a club format",
                        "https://upload.wikimedia.org/wikipedia/commons/c/cf/Fight_Club_Soap_%286624162303%29.jpg",
                        "https://www.youtube.com/watch?v=SUXWAEX2jlg")
#creates the fight clube instance of the class movie

movies = [matrix, signs, fight_club]
#creates a list of the movie class instances
fresh_tomatoes.open_movies_page(movies)
#calls fresh_tomatoes to open the movie page

