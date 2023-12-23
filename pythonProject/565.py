# movies = {
#     "Django Unchained": {
#         "John": 10,
#         "Jack": 9
#     },
#     "Troy": {}
# }
#
# def add_movie(movie_name):
#     movie_name = movie_name.capitalize()
#     if movie_name not in movies:
#         movies[movie_name] = {}
#         print("Movie added successfully")
#     else:
#         print("This movie already exists!")
#
# def add_rating(movie_name, user_name, rating):
#     movie = find_movie(movie_name)
#     if movie:
#         while user_name in movie:
#             user_name = input("This user already rated the movie. Enter a different username: ")
#         if movie_name in movies:
#             if 0 <= rating <= 10:
#                 movie[user_name] = rating
#                 print(f"A rating has been added for {movie_name}: {user_name} rated it {rating}")
#             else:
#                 print("Invalid rating. Rating should be between 0 and 10.")
#     else:
#         print("This movie doesn't exist")
#
# def find_movie(movie_name):
#     movie_name = movie_name.capitalize()
#     return movies.get(movie_name)
#
# def display_ratings():
#     for movie_name, ratings in movies.items():
#         if ratings:
#             average_rating = sum(ratings.values()) / len(ratings)
#             print(f"{movie_name} is rated {average_rating:.1f}")
#         else:
#             print(f"Rating is not yet available for {movie_name}")
#
# def main():
#     while True:
#         print("\n1. Add Movie\n2. Add Rating\n3. Display Ratings\n4. Exit")
#         choice = input("Enter your choice (1-4): ")
#
#         if choice == '1':
#             movie_name = input("Enter the movie name: ")
#             add_movie(movie_name)
#             print(movies)
#         elif choice == '2':
#             movie_name = input("Enter the movie name: ")
#             user_name = input("Enter your name: ")
#             rating = float(input("Enter your rating (0-10): "))
#             add_rating(movie_name, user_name, rating)
#             print(movies)
#         elif choice == '3':
#             display_ratings()
#
#         elif choice == '4':
#             print("Exiting the program. Goodbye!")
#             break
#         else:
#             print("Invalid choice. Please enter a number between 1 and 4.")
#
# if __name__ == "__main__":
#     main()
class Computer:
    def __init__(self, cpu, memory):
        self.__cpu = cpu
        self.__memory = memory

    # Геттеры и сеттеры для cpu
    @property
    def cpu(self):
        return self.__cpu

    @cpu.setter
    def cpu(self, value):
        self.__cpu = value

    # Геттеры и сеттеры для memory
    @property
    def memory(self):
       return self.__memory

    @memory.setter
    def memory(self, value):
        self.__memory = value

    def make_computations(self):
        # Производим какие-то вычисления на основе cpu и memory
        result = f"Computations using CPU {self.__cpu} and Memory {self.__memory}"
        return result

    def __str__(self):
        return f"Computer: CPU - {self.__cpu}, Memory - {self.__memory}"


class Phone:
    def __init__(self, sim_cards_list):
        self.__sim_cards_list = sim_cards_list

    # Геттер и сеттер для sim_cards_list
    @property
    def sim_cards_list(self):
        return self.__sim_cards_list

    @sim_cards_list.setter
    def sim_cards_list(self, value):
        self.__sim_cards_list = value

    def call(self, sim_card_number, call_to_number):
        # Симуляция звонка на основе номера сим-карты
        result = f"Calling {call_to_number} from SIM Card-{sim_card_number}"
        return result

    def __str__(self):
        return f"Phone: SIM Cards - {self.__sim_cards_list}"


class SmartPhone(Computer, Phone):
    def __init__(self, cpu, memory, sim_cards_list):
        Computer.__init__(self, cpu, memory)
        Phone.__init__(self, sim_cards_list)

    def use_gps(self, location):
        # Симуляция использования GPS
        result = f"Using GPS to navigate to {location}"
        return result

    def __str__(self):
        return f"SmartPhone: CPU - {self.__cpu}, Memory - {self.__memory}, SIM Cards - {self.__sim_cards_list}"


# Создаем объекты
computer_obj = Computer(cpu="Intel i5", memory=8)
phone_obj = Phone(sim_cards_list=["Beeline", "Megafon"])
smartphone1_obj = SmartPhone(cpu="Snapdragon", memory=4, sim_cards_list=["MTS", "Tele2"])
smartphone2_obj = SmartPhone(cpu="Apple A14 Bionic", memory=16, sim_cards_list=["Vodafone", "T-Mobile"])

# Распечатываем информацию
print(computer_obj)
print(phone_obj)
print(smartphone1_obj)
print(smartphone2_obj)

# Опробовываем методы
print(computer_obj.make_computations())
print(phone_obj.call(1, "+996 777 99 88 11"))
print(smartphone1_obj.use_gps("Home"))

# Магические методы сравнения в Computer
print(computer_obj == SmartPhone("AMD Ryzen", 16, ["A1", "Sprint"]))  # Использует __eq__
print(computer_obj != SmartPhone("Intel i5", 8, ["Verizon", "AT&T"]))  # Использует __ne__
print(computer_obj > SmartPhone("ARM Cortex", 32, ["O2", "Three"]))  # Использует __gt__
print(computer_obj < SmartPhone("Snapdragon", 4, ["Orange", "EE"]))  # Использует __lt__
print(computer_obj >= SmartPhone("Intel i5", 8, ["Bell", "Rogers"]))  # Использует __ge__
print(computer_obj <= SmartPhone("AMD Ryzen", 16, ["T-Mobile", "Sprint"]))