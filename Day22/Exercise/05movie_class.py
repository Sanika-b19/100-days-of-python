# Exercise 5: Create a Movie Class with Methods

class Movie:
    def __init__(self, title, director, year, rating):
        self.title = title
        self.director = director
        self.year = year
        self.rating = rating

    def update_rating(self, new_rating):
        self.rating = new_rating

    def display(self):
        print(f"Movie: {self.title}")
        print(f"Directed by: {self.director}")
        print(f"Year: {self.year}")
        print(f"Rating: {self.rating}/10")

movie = Movie("Inception", "Christopher Nolan", 2010, 8.8)
movie.update_rating(9.0)
movie.display()
