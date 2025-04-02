from flask import Flask, render_template

app = Flask(__name__)

movies = [
  {
    "name": "Inside Out 2",
    "genre": "Animation, Comedy, Drama",
    "trailer": "https://www.youtube.com/watch?v=LEjhY15eCx0",
    "poster": "https://upload.wikimedia.org/wikipedia/en/f/f7/Inside_Out_2_poster.jpg"
  },
  {
    "name": "Deadpool & Wolverine",
    "genre": "Action, Comedy, Sci-Fi",
    "trailer": "https://www.youtube.com/watch?v=73_1biulkYk",
    "poster": "https://upload.wikimedia.org/wikipedia/en/4/4c/Deadpool_%26_Wolverine_poster.jpg"
  },
  {
    "name": "Dune: Part Two",
    "genre": "Adventure, Drama, Sci-Fi",
    "trailer": "https://www.youtube.com/watch?v=Way9Dexny3w",
    "poster": "https://upload.wikimedia.org/wikipedia/en/5/52/Dune_Part_Two_poster.jpeg"
  },
  {
    "name": "Wicked",
    "genre": "Fantasy, Musical, Romance",
    "trailer": "https://www.youtube.com/watch?v=6COmYeLsz4c",
    "poster": "https://m.media-amazon.com/images/M/MV5BOWMwYjYzYmMtMWQ2Ni00NWUwLTg2MzAtYzkzMDBiZDIwOTMwXkEyXkFqcGc@._V1_FMjpg_UX1000_.jpg"
  },
  {
    "name": "Anora",
    "genre": "Comedy, Drama, Romance",
    "trailer": "https://www.youtube.com/watch?v=GuPkfvxmtdw",
    "poster": "https://upload.wikimedia.org/wikipedia/en/2/2b/Anora_%282024_film%29_poster.jpg"
  },
  {
    "name": "The Brutalist",
    "genre": "Drama",
    "trailer": "https://www.youtube.com/watch?v=GdRXPAHIEW4",
    "poster": "https://m.media-amazon.com/images/M/MV5BM2U0MWRjZTMtMDVhNC00MzY4LTgwOTktZGQ2MDdiYTI4OWMxXkEyXkFqcGc@._V1_FMjpg_UX1000_.jpg"
  },
  {
    "name": "Challengers",
    "genre": "Comedy, Drama, Romance, Sport",
    "trailer": "https://www.youtube.com/watch?v=VobTTbg-te0",
    "poster": "https://upload.wikimedia.org/wikipedia/en/b/b4/Challengers_2024_poster.jpeg",
  },
  {
    "name": "The Bikeriders",
    "genre": "Crime, Drama",
    "trailer": "https://www.youtube.com/watch?v=BrSaVt5pvPk",
    "poster": "https://m.media-amazon.com/images/M/MV5BZDY3MGVjYjItN2I1OC00ZGNkLWIwOGQtNTBiNWM1NmQ5NTZlXkEyXkFqcGc@._V1_FMjpg_UX1000_.jpg"
  },
  {
    "name": "Megalopolis",
    "genre": "Drama, Fantasy, Sci-Fi",
    "trailer": "https://www.youtube.com/watch?v=pq6mvHZU0fc",
    "poster": "https://upload.wikimedia.org/wikipedia/en/f/f3/Megalopolis_%28film%29_poster.jpg"
  },
  {
    "name": "The Watchers",
    "genre": "Fantasy, Horror, Mystery, Thriller",
    "trailer": "https://www.youtube.com/watch?v=dYo91Fq9tKY",
    "poster": "https://upload.wikimedia.org/wikipedia/en/thumb/b/b7/The_Watchers_film_poster.jpg/220px-The_Watchers_film_poster.jpg"
  }
]

@app.route("/")
def home():
    return render_template("index.html", title="Nitflex", movies=movies)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=6060)
