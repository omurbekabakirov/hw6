movies = {

    "Django Unchained": {

        "John": 10,

        "Jack": 9

    },

    "Troy": {}

}
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
    elif user_name in movies[movie_name]:
        print("This user already exists. ")
    else:
        try:
            rating = int(rating)
            if 0 <= rating <= 10:
                movies[movie_name][user_name] = rating
                print(f"A rating has been added for {movie_name}: {user_name} rated it {rating}")
            else:
                print("Invalid rating. Please enter a rating between 0 and 10.")
        except ValueError:
                    print("Invalid rating. Please enter a valid number.")


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



while True:
    print("\n1. Add Movie\n2. Add Rating\n3. View Ratings\n4. Exit")
    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        movie_name = input("Enter the movie name: ")
        add_movie(movies, movie_name)
        print(movies)
    elif choice == "2":
        movie_name = input("Enter the movie name: ").title()
        if movie_name in movies:
            user_name = input("enter user name: ")
            rating = input("enter rating: ")
            add_rating(movies, movie_name, user_name, rating)
        print(movies)

    elif choice == "3":
        view_ratings(movies)
    elif choice == "4":
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")











