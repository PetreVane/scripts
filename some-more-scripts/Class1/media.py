import webbrowser

class Movie():

	" " " This is documentation for this Class " " "

	valid_ratings = ["G", "PG", "PG-13", "R" ]

	def __init__(self, movie_title, storyline, poster_image, trailer_youtube):
		self.title = movie_title
		self.storyline = storyline
		self.poster_image_url = poster_image
		self.trailer_youtube_url = trailer_youtube


	def show_trailer(self):
		webbrowser.open(self.trailer_youtube_url)
