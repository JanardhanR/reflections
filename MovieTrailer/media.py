import webbrowser

class Movie(): #google style https://google.github.io/styleguide/pyguide.html for good programming practices
    """ This class provides a way to store members"""
    VALID_RATINGS = ["G","PG","PG-13","R"]
    # double underlines indicate reserved names
    # self - reference to itself.  though self if meaning full any other word can be used instead
    def __init__ (self, movie_title,
                  movie_storyline,
                  poster_image,
                  trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
