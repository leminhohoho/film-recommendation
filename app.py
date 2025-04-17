from flask import Flask, render_template, request
import collab_filtering

app = Flask(__name__)

user = [0] * 250


@app.route("/")
def home():

    movies = collab_filtering.get_movies(user)

    return render_template("index.html", title="Nitflex", movies=movies)


@app.route("/movies")
def movies():
    movieIndex = request.args.get("movie")
    rating = request.args.get("rating")
    if movieIndex != None and rating != None:
        user[int(movieIndex)] = int(rating)

    return f"Movie Index: {movieIndex}, Rating: {rating}"


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=6060)
