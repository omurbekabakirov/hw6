import sqlite3


def create_connection(db_name):
    connection = None
    try:
        conn = sqlite3.connect(db_name)
    except sqlite3.Error as e:
        print(e)
    return conn


def create_table(connection, sql):
    try:
        cursor = connection.cursor()
        cursor.execute(sql)
    except sqlite3.Error as e:
        print(e)


def insert_country(connection, country):
    sql = 'INSERT INTO countries(title) VALUES (?)'
    try:
        cursor = connection.cursor()
        cursor.execute(sql, country)
        connection.commit()
    except sqlite3.Error as e:
        print(e)


def insert_city(connection, city):
    sql = '''INSERT INTO cities(title, area, country_id) VALUES (?, ?, ?)'''
    try:
        cursor = connection.cursor()
        cursor.execute(sql, city)
        connection.commit()
    except sqlite3.Error as e:
        print(e)


def insert_student(connection, students):
    sql = '''INSERT INTO students (first_name,last_name, city_id) VALUES (?, ?, ?)'''
    try:
        cursor = connection.cursor()
        cursor.execute(sql, students)
        connection.commit()
    except sqlite3.Error as e:
        print(e)


def show_cities(connection):
    try:
        cursor = connection.cursor()
        cursor.execute('SELECT id, title FROM cities')
        cities = cursor.fetchall()
        for city in cities:
            print(f"{city[0]}. {city[1]}")
    except sqlite3.Error as e:
        print(e)


def show_students_by_city(connection, city_id):
    try:
        cursor = connection.cursor()
        cursor.execute('''
            SELECT students.first_name, students.last_name, countries.title, cities.title, cities.area
            FROM students
            JOIN cities ON students.city_id = cities.id
            JOIN countries ON cities.country_id = countries.id
            WHERE cities.id = ?
        ''', (city_id,))
        students = cursor.fetchall()
        if students:
            print("\nСтуденты в выбранном городе:")
            for student in students:
                print(f"Имя: {student[0]} {student[1]}, Страна: {student[2]}, Город: {student[3]}, Площадь: {student[4]}")
        else:
            print("В выбранном городе нет студентов.")
    except sqlite3.Error as e:
        print(e)


sql_create_table = '''CREATE TABLE countries(
id INTEGER PRIMARY KEY AUTOINCREMENT,
title VARCHAR(200) NOT NULL)'''

sql_create_table2 = '''CREATE TABLE cities(
id INTEGER PRIMARY KEY AUTOINCREMENT,
title VARCHAR(200) NOT NULL,
area FLOAT DEFAULT 0,
country_id INTEGER REFERENCES countries(id) ON DELETE CASCADE)'''

sql_create_table3 = '''CREATE TABLE students(
id INTEGER PRIMARY KEY AUTOINCREMENT,
first_name VARCHAR(200) NOT NULL ,
last_name VARCHAR(200) NOT NULL ,
city_id INTEGER REFERENCES cities(id) ON DELETE CASCADE
)'''

my_connection = create_connection("hw8.db")

if my_connection is not None:
    print("Connected to SQLite successfully!")
    create_table(my_connection, sql_create_table)
    create_table(my_connection, sql_create_table2)
    create_table(my_connection, sql_create_table3)

    insert_country(my_connection, ('France',))
    insert_country(my_connection, ('Italy',))
    insert_country(my_connection, ('Russia',))

    insert_city(my_connection, ('Rome', 234.5, 2))
    insert_city(my_connection, ('Paris', 250.5, 1))
    insert_city(my_connection, ('Moscow', 264.5, 3))
    insert_city(my_connection, ('Marseille', 224.5,2))
    insert_city(my_connection, ('Venice', 214.5,2))
    insert_city(my_connection, ('Florence', 239.5,1))
    insert_city(my_connection, ('Peter Burg', 284.5,3))

    insert_student(my_connection, ('Max','Koralov',1))
    insert_student(my_connection, ('Petr','1',2))
    insert_student(my_connection, ('Adolf','Gitler',3))
    insert_student(my_connection, ('Cris','Cris',4))
    insert_student(my_connection, ('Oma','Abakirov',5))
    insert_student(my_connection, ('Dima','Soikin',6))
    insert_student(my_connection, ('Sasha','Pavlova',7))
    insert_student(my_connection, ('Kiril','Karpov',3))
    insert_student(my_connection, ('Kenpachi','Zarraki',7))
    insert_student(my_connection, ('Masha','Koralova',1))
    insert_student(my_connection, ('Dasha','Koralova',1))
    insert_student(my_connection, ('Grisha','Koralova',2))
    insert_student(my_connection, ('Natasha','Koralova',3))
    insert_student(my_connection, ('Sophia','Koralova',4))
    insert_student(my_connection, ('Frank','Djonson',7))

    while True:
        print("\nВы можете отобразить список студентов, выбрав ID города:")
        show_cities(my_connection)
        try:
            city_id = int(input("Введите ID города (0 для выхода): "))
            if city_id == 0:
                break
            elif 1 <= city_id <= 7:
                show_students_by_city(my_connection, city_id)
            else:
                print("Неверный ID города. Пожалуйста, повторите попытку.")
        except ValueError:
            print("Неверный ввод. Введите корректный ID города.")

    my_connection.close()
