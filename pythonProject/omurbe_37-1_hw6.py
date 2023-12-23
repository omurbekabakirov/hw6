def add_movie(movies, movie_name):
    movie_name = movie_name.capitalize()
    if movie_name not in movies:
        movies[movie_name] = {}
        print("Movie added successfully")
    else:
        print("This movie already exists!")

def add_rating(movies, movie_name, user_name, rating):
    movie_name = movie_name.capitalize()
    if movie_name not in movies:
        print("This movie doesn't exist")
        return

    while user_name in movies[movie_name]:
        user_name = input("This user already exists. Please enter a different user name: ")

    if 0 <= rating <= 10:
        movies[movie_name][user_name] = rating
        print(f"A rating has been added for {movie_name}: {user_name} rated it {rating}")
    else:
        print("Invalid rating. Please enter a rating between 0 and 10.")

def view_ratings(movies):
    for movie_name, ratings in movies.items():
        if not ratings:
            print(f"Rating is not yet available for {movie_name}")
        else:
            average_rating = sum(ratings.values()) / len(ratings)
            print(f"{movie_name} is rated {average_rating:.1f}")

def find_movie(movies, movie_name):
    movie_name = movie_name.capitalize()
    return movies.get(movie_name, None)

movies = {
    "Django Unchained": {"John": 10, "Jack": 9},
    "Troy": {}
}

while True:
    print("\n1. Add Movie\n2. Add Rating\n3. View Ratings\n4. Exit")
    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        movie_name = input("Enter the movie name: ")
        add_movie(movies, movie_name)
        print(movies)
    elif choice == "2":
        movie_name = input("Enter the movie name: ")
        movie = find_movie(movies, movie_name)
        if movie:
            user_name = input("Enter the user name: ")
            rating = float(input("Enter the rating (0-10): "))
            add_rating(movies, movie_name, user_name, rating)
    elif choice == "3":
        view_ratings(movies)
    elif choice == "4":
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")




