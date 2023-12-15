class Person:
    def __init__(self, tolerance):
        self.tolerance = tolerance

    def buy_ticket(self, room):
        if room.total_duration() < 120 and len(room.people) < 100:
            room.people.append(self)

    def watch_movie(self, movie):
        self.tolerance -= movie.calculate_rejection(len(movie.room.people))
        if self.tolerance <= 0:
            movie.room.people.remove(self)

    def become_cinephile(self):
        self.__class__ = Cinephile

class Cinephile(Person):
    def watch_movie(self, movie):
        self.tolerance -= movie.calculate_rejection(len(movie.room.people)) / 2
        if self.tolerance <= 0:
            movie.room.people.remove(self)

class Fanatic(Person):
    def watch_movie(self, movie):
        rejection = movie.calculate_rejection(len(movie.room.people))
        if rejection > 30:
            self.tolerance -= rejection
        if self.tolerance <= 0:
            movie.room.people.remove(self)

class Movie:
    def __init__(self, duration, room):
        self.duration = duration
        self.room = room

    def calculate_rejection(self, people_count):
        pass

class Bizarre(Movie):
    def calculate_rejection(self, people_count):
        return people_count

class DeTerror(Movie):
    def calculate_rejection(self, people_count):
        return self.duration / 5 * 3

class ClaseZ(Movie):
    def calculate_rejection(self, people_count):
        return 2

class Ultraviolent(DeTerror):
    def calculate_rejection(self, people_count):
        return super().calculate_rejection(people_count) * 2

class Room:
    def __init__(self):
        self.movies = []
        self.people = []

    def total_duration(self):
        return sum(movie.duration for movie in self.movies)

    def project_movie(self, movie):
        for person in self.people:
            person.watch_movie(movie)
        for person in self.people:
            person.become_cinephile()

class Cinema:
    def __init__(self):
        self.rooms = []

    def average_tolerance(self):
        people = [person for room in self.rooms for person in room.people]
        return sum(person.tolerance for person in people) / len(people) if people else 0

    def bloody_rooms(self):
        return [room for room in self.rooms if any(movie.calculate_rejection(len(room.people)) >= 50 for movie in room.movies)]


# ************************ PRUEBAS ************************

# Create a cinema
cinema = Cinema()

# Create some rooms in the cinema
room1 = Room()
room2 = Room()
cinema.rooms.extend([room1, room2])

# Create some movies
movie1 = Bizarre(60, room1)
movie2 = DeTerror(90, room1)
movie3 = ClaseZ(50, room2)
movie4 = Ultraviolent(120, room2)

# Add the movies to the rooms
room1.movies.extend([movie1, movie2])
room2.movies.extend([movie3, movie4])

# Create some people
person1 = Person(100)
person2 = Cinephile(200)
person3 = Fanatic(300)

# People buy tickets for the rooms
person1.buy_ticket(room1)
person2.buy_ticket(room1)
person3.buy_ticket(room2)

# Project the movies in the rooms
for movie in room1.movies:
    room1.project_movie(movie)

for movie in room2.movies:
    room2.project_movie(movie)

# Print the average tolerance in the cinema
print(cinema.average_tolerance())

# Print the bloody rooms in the cinema
print(cinema.bloody_rooms())