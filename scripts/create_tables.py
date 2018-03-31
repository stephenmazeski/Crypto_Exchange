import psycopg2
import sys

def create_and_populate_tables():

    #Define our connection parameters
    conn_string = "host='localhost' dbname='postgres' user='postgres' password='password'"

    #Connect to database
    conn = psycopg2.connect(conn_string)

    #Initialize cursor
    cur = conn.cursor()

    creates = (
        """CREATE TABLE users (
            user_id SERIAL PRIMARY KEY,
            username VARCHAR(20) UNIQUE,
            password VARCHAR(30),
            email VARCHAR(50) UNIQUE)""",

        """CREATE TABLE questions (
                question_id SERIAL PRIMARY KEY,
                user_id INT REFERENCES users(user_id),
                question_summary VARCHAR(255) NOT NULL,
                question_desc VARCHAR(1000),
                category VARCHAR(30))""",

        """CREATE TABLE comments (
                comment_id SERIAL PRIMARY KEY,
                user_id INT REFERENCES users(user_id),
                question_id INT REFERENCES questions(question_id),
                comment_text VARCHAR(1000) NOT NULL)""",

        """CREATE TABLE open_orders(
                order_id SERIAL PRIMARY KEY,
                coin_id_out varchar(3),
                coin_id_in varchar(3),
                ordertype varchar(4),
                amount_out DECIMAL(12,8),
                amount_in DECIMAL(12,8))""" ,

        """CREATE TABLE categories(
                category_id SERIAL PRIMARY KEY,
                category_name VARCHAR[30],
                parent_category INT REFERENCES categories(category_id))""",


        """INSERT INTO users (username, password, email) VALUES
            ('alex1996', 'password1', 'asdf1@gmail.com'),
            ('alex1995', 'password2', 'asdf2@gmail.com'),
            ('alex1994', 'password3', 'asdf3@gmail.com'),
            ('alex1993', 'password4', 'asdf4@gmail.com')""",

        """INSERT INTO questions (user_id, question_summary, question_desc, category) VALUES
            (3, 'This is a question summary... Cool shit bruh', 'This description is dank', 'Memes'),
            (3, 'This question summary is cool shit bruh', 'This is a dank description', 'Memes'),
            (2, 'Question: is this summary cool shit bruh?', 'More like a dank prescription', 'Memes'),
            (1, 'This cool question summary is shit bruh', 'You can take this description to the bank', 'Memes')
            """,

        """INSERT INTO comments (user_id, question_id, comment_text) VALUES
            (4, 1, 'This comment is for the dank question'),
            (2, 1, 'This comment is another for the dank question'),
            (1, 1, 'This comment  yet another for the dank question'),
            (3, 1, 'This comment is the fourth for the dank question'),
            (3, 1, 'This comment is the final for the dank question')
        """,
        """INSERT INTO open_orders (user_id, coin_id_out, coin_id_in, amount_out, amount_in) VALUES
            (1, 'BTC', 'ETH', 2.09318018, 8.39184928),
            (3, 'BTC', 'ETH', 2.19385710, 0.12390193),
            (2, 'BTC', 'ETH', 1.29301923, 0.34902333),
            (1, 'NEO', 'LTC', 72.93480192, 281.39849238),
            (1, 'ETH', BTC, 2.39892833, 8.17364928),
            (2, 'LTC', 'NEO', 8.17364928, 2.39892833)
            """

#user_id in will have to go back into open_orders
    selects = (
        "SELECT * FROM users,
        "SELECT * FROM questions",
        "SELECT * FROM comments"
        "SELECT * FROM open_orders"
    )

    for create in creates:
        cur.execute(create)

    for select in selects:
        cur.execute(select)
        rows = cur.fetchall()
        for row in rows:
            print(row)


    #Destroy connection
    cur.close()
    conn.commit()
    conn.close()

create_and_populate_tables()
