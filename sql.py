# ACID

# Atomicity
# Consistency
# Isolation
# Durability
from pprint import pprint

import sqlite3
from sqlite3 import Error


def create_connection(path: str):
    connection = None
    try:
        connection = sqlite3.connect(path)
    except Error as e:
        print(f'Sqlite connectio error {e}')

    return connection


def execute_query(connection, query: str):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
    except Error as e:
        print(f'Sqlite connectio error {e}')


connection = create_connection('my_db.sqlite')

create_users_table = """
CREATE TABLE IF NOT EXISTS users (
    id  INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER,
    gender VARCHAR(10),
    location TEXT
);
"""

create_posts_table = """
CREATE TABLE IF NOT EXISTS posts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    description TEXT NOT NULL,
    user_id INTEGER NOT NULL, 
    FOREIGN KEY (user_id) REFERENCES users (id)
)
"""

execute_query(connection, create_users_table)
execute_query(connection, create_posts_table)

create_comments_table = """
CREATE TABLE IF NOT EXISTS comments (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    text TEXT NOT NULL,
    user_id INTEGER NOT NULL, 
    post_id INTEGER NOT NULL, 
    FOREIGN KEY (user_id) REFERENCES users (id)
    FOREIGN KEY (post_id) REFERENCES posts (id)
)
"""

create_likes_table = """
CREATE TABLE IF NOT EXISTS likes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL, 
    post_id INTEGER NOT NULL, 
    FOREIGN KEY (user_id) REFERENCES users (id)
    FOREIGN KEY (post_id) REFERENCES posts (id)
)
"""

execute_query(connection, create_comments_table)
execute_query(connection, create_likes_table)

create_users = """
INSERT INTO 
    users (name, age, gender, location)
VALUES 
    ('Oleg', 31, 'male', 'Zhmerynka'),
    ('Yurii', 36, 'male', 'Kmemenchug'),
    ('Tetiana', 24, 'female', 'Poltava'),
    ('Lev', 25, 'male', 'Odesa'),
    ('Olga', 27, 'female', 'Odesa');
"""

create_posts = """
INSERT INTO
    posts (title, description, user_id)
VALUES 
    ('Щастя', 'Сьогодні я щасливий', 1),
    ('Спекотно', 'Сьогодні дуже спекотно', 2),
    ('Допомога', 'Допоможіть мені розібратись з SQL', 3),
    ('Гарні новини', 'Я отримав сертифікат від Бітрут', 4),
    ('Вечірка', 'Хто зі мною на вечірку?', 5)
"""

# execute_query(connection, create_users)
# execute_query(connection, create_posts)

create_comments = """
INSERT INTO 
    comments (text, user_id, post_id)
VALUES 
    ('Я готовий', 1, 5),
    ('Що саме не зрозуміо?', 5, 3),
    ('Дуже радий за тебе', 2, 4),
    ('Мої вітання', 3, 4),
    ('Вітаю Олег', 4, 1);
"""

create_likes = """
INSERT INTO
    likes (user_id, post_id)
VALUES 
    (1, 1),
    (1, 4),
    (2, 3),
    (2, 1),
    (3, 4),
    (4, 5), 
    (5, 3);
"""

# execute_query(connection, create_comments)
# execute_query(connection, create_likes)
###############################################################################
# SELECT


def select_query(connection, query: str):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f'Sqlite connection error {e}')


select_users = "SELECT * from users"

users = select_query(connection, select_users)

# pprint(users)

posts = "SELECT * from posts"

posts = select_query(connection, posts)

# pprint(posts)

select_users_posts = """
SELECT 
    users.id,
    users.name,
    posts.description
FROM
    posts
INNER JOIN users on users.id = posts.user_id
"""

users_posts = select_query(connection, select_users_posts)

# pprint(users_posts)

select_posts_comments_users = """
SELECT
    posts.description as post,
    text as comment,
    name
FROM
    posts
    INNER JOIN comments on posts.id = comments.post_id
    INNER JOIN users on users.id = comments.user_id
"""

result = select_query(connection, select_posts_comments_users)

# pprint(result)

where_select = "SELECT description FROM posts WHERE id = 2"

result = select_query(connection, where_select)
# pprint(result)

if __name__ == '__main__':
    ...
