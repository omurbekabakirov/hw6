import sqlite3
def create_connection(hw_db):
    connection = None
    try:
        connection = sqlite3.connect(hw_db)
    except sqlite3.Error as e:
        print(e)
    return connection

sql_create_table = '''
CREATE TABLE products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_title VARCHAR(200) NOT NULL,
    price DOUBLE(10,2) NOT NULL DEFAULT 0.0,
    quantity INTEGER(8) NOT NULL DEFAULT 0)'''


def create_table(connection,sql):
    try:
        cursor = connection.cursor()
        cursor.execute(sql)
    except sqlite3.Error as e:
        print(e)
my_connection = create_connection('hw.db')

def insert_product(connection,products):
    try:
        sql = ('''INSERT INTO products (product_title, price, quantity)
                   VALUES (?,?,?)''')
        cursor = connection.cursor()
        cursor.execute(sql,products)
        connection.commit()
    except sqlite3.Error as e:
        print(e)
def change_quantity_products(connection,change_quantity):
    try:
        sql = '''UPDATE products SET quantity = ? WHERE id = ?'''
        cursor = connection.cursor()
        cursor.execute(sql, change_quantity)
        connection.commit()
    except sqlite3.Error as e:
        print(e)
def change_price_products(connection,change_price):
    try:
        sql = '''UPDATE products SET price = ? WHERE id = ?'''
        cursor = connection.cursor()
        cursor.execute(sql, change_price)
        connection.commit()
    except sqlite3.Error as e:
        print(e)
def delete_products(connection,delete_id):
    try:
        sql = '''DELETE FROM products WHERE id = ?'''
        cursor = connection.cursor()
        cursor.execute(sql,(delete_id,))
        connection.commit()
    except sqlite3.Error as e:
        print(e)
def select_products(connection):
    try:
        sql = '''SELECT * FROM products '''
        cursor = connection.cursor()
        cursor.execute(sql)
        rows = cursor.fetchall()
        for row in rows:
            print(row)
        connection.commit()
    except sqlite3.Error as e:
        print(e)
def select_products_by_price_and_quantity(connection):
    try:
        sql = '''SELECT * FROM products WHERE price < 100  AND quantity > 5'''
        cursor = connection.cursor()
        cursor.execute(sql)
        rows = cursor.fetchall()
        for row in rows:
            print(row)
        connection.commit()
    except sqlite3.Error as e:
        print(e)
def find_by_word(connection,word):
    try:
        sql = '''SELECT * FROM products WHERE product_title LIKE ?'''
        cursor = connection.cursor()
        cursor.execute(sql,('%' + word + '%',))
        rows = cursor.fetchall()
        for row in rows:
            print(row)
        connection.commit()
    except sqlite3.Error as e:
        print(e)
if my_connection is not None:
    print('Connected to SQLite database')
    create_table(my_connection, sql_create_table)
    insert_product(my_connection,('Жидкое мыло',60.60,4))
    insert_product(my_connection,('potatoe',78.09,5))
    insert_product(my_connection,('peach',78.09,4))
    insert_product(my_connection,('apple',68.09,1))
    insert_product(my_connection,('orange',56.09,8))
    insert_product(my_connection,('meat',12.09,6))
    insert_product(my_connection,('candy',678.09,3))
    insert_product(my_connection,('rice',34.09,4))
    insert_product(my_connection,('pineapple',99.09,4))
    insert_product(my_connection,('pear',87.09,7))
    insert_product(my_connection,('mandarins',55.09,87))
    insert_product(my_connection,('abricot',67.09,43))
    insert_product(my_connection,('watermelon',88.09,45))
    insert_product(my_connection,('melon',667.09,4354))
    insert_product(my_connection,('pumpkin',167.08,4354))
    insert_product(my_connection, ('eggplant', 12345678.09, 4354))
    change_quantity_products( my_connection,(50,1))
    change_price_products(my_connection,(35.56,1))
    delete_products(my_connection,2)
    select_products(my_connection)
    select_products_by_price_and_quantity(my_connection)
    find_by_word(my_connection ,'мыло')
    my_connection.close()
