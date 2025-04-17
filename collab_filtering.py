import math
import utils


def get_movies(user: list[int]):
    # user data but only contain unwatched movies
    user_unwatched_movies = [0.0] * 250
    top_users = []

    with open("users.csv", "r") as file:
        data = file.read()
        csvContent = data.split("\n")[1:]
        userbase = list(map(utils.convert_to_list, csvContent))

        top_users = get_most_similar_users(user, userbase, 5)

        for movie_index in range(0, len(user)):
            if user[movie_index] == 0:
                user_unwatched_movies[movie_index] = predict_value(
                    user,
                    top_users,
                    movie_index,
                )

    # List of movie indices sort based on the predicted values
    movie_indices = []
    for index in range(0, len(user_unwatched_movies)):
        movie_indices.append(index)

    # Sort the list of movie based on the predicted values
    def sort_func(index):
        return user_unwatched_movies[index]

    movie_indices.sort(key=sort_func, reverse=True)

    # Import the movie list
    with open("movies.csv", "r") as file:
        data = file.read()
        csvContent = data.split("\n")[1:]
        movies = []

        for movie_index in movie_indices:
            movie = csvContent[movie_index][1:-1]
            movieProperties = movie.split('","')
            movies.append(
                {
                    "movie_index": movie_index,
                    "name": movieProperties[0],
                    "genre": movieProperties[1],
                    "trailer": movieProperties[2],
                    "poster": movieProperties[3],
                }
            )

    return movies


def dot_product(v1: list[int], v2: list[int]) -> float:
    val = 0
    for i in range(0, len(v1)):
        val += v1[i] * v2[i]

    return val


def cosine_similarity(u1: list[int], u2: list[int]) -> float:
    if dot_product(u1, u1) == 0:
        return 0

    return dot_product(u1, u2) / (
        math.sqrt(dot_product(u1, u1)) * math.sqrt(dot_product(u2, u2))
    )


def get_most_similar_users(
    u1: list[int], userbase: list[list[int]], top: int
) -> list[list[int]]:
    def sort_func(u: list[int]) -> float:
        return cosine_similarity(u1, u)

    most_similar_users = userbase.copy()
    most_similar_users.sort(key=sort_func, reverse=True)
    most_similar_users = most_similar_users[:top]

    return most_similar_users


def predict_value(u1: list[int], top_users: list[list[int]], movie_index: int) -> float:
    numerator = 0
    denominator = 0

    # Compute the predicting value from the selected users
    for u in top_users:
        numerator += cosine_similarity(u1, u) * u[movie_index]
        denominator += cosine_similarity(u1, u)

    if numerator == 0 and denominator == 0:
        return 0

    return numerator / denominator
