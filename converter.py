import json

movies = ""

with open("movies.json", "r") as file:
    movies = json.loads(file.read()) 

movieCSV = "name,genre,trailer,poster"
userCSV = ""

for movie in  movies:
    name = movie["primaryTitle"]
    genre = ",".join( movie["genres"] )
    trailer = movie["trailer"]
    poster = movie["primaryImage"]

    movieCSV += "\n"
    movieRow = [ 
        f'"{name}"',
        f'"{genre}"',
        f'"{trailer}"',
        f'"{poster}"',
    ] 

    movieCSV +=",".join(movieRow)

def getMovieName(movie):
    return movie["primaryTitle"]

userCSV = ",".join(map(getMovieName, movies))

with open("movies.csv", "w") as file:
    file.write(movieCSV)

with open("user.csv", "w") as file:
    file.write(userCSV)
