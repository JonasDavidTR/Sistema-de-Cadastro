import mysql.connector
from mysql.connector import Error


def con():
    con = None
    try:
        con = mysql.connector.connect(
            host = 'localhost',
            database = 'python',
            user = 'root',
            passwd = ''
        )
    except Error as er:
        print(er)
    finally:
        return con


def close(con):
    return con.close()
