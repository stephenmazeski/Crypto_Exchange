import psycopg2
import sys

def main():
    #Define our connection string
    conn_string = "host='localhost' dbname='projectoutline' user='postgres' password='Xana42169!!!'"

    # print the connection string we will use to connect
    #print "Connecting to database\n	->%s" % (conn_string)

    # get a connection, if a connect cannot be made an exception will be raised here
    conn = psycopg2.connect(conn_string)

    # conn.cursor will return a cursor object, you can use this cursor to perform queries
    cur = conn.cursor()
    print("Connected!")
    commands = (
    """DROP TABLE comments
    """,
    """DROP TABLE questions
    """
    )
    for command in commands:
        cur.execute(command)
    cur.close()
    conn.commit()
    conn.close()

if __name__ == "__main__":
    main()