import os
import sqlite3
from functools import wraps

from personal_website.constants import DATABASE_NAME

conn = None


def database_call(func):
    @wraps(func)
    def decorated_function(*args, **kwargs):
        global conn
        conn = sqlite3.connect(DATABASE_NAME)
        ret_val = func(*args, **kwargs)
        conn.commit()
        conn.close()
        return ret_val

    return decorated_function


@database_call
def create_table_minified():
    conn.execute(
        '\n'
        'CREATE TABLE IF NOT EXISTS \n'
        'minified (id INTEGER, name TEXT, content TEXT, type TEXT)'
    )


@database_call
def insert_dummy_into_minified():
    cursor = conn.cursor()
    cursor.execute("INSERT INTO  minified VALUES "
                 "(0, '', '', '')")


def create_initial_database():
    create_table_minified()
    insert_dummy_into_minified()


def wipe_database():
    os.remove(DATABASE_NAME)


class MinifiedRepo:
    @staticmethod
    @database_call
    def get_max_id():
        cursor = conn.cursor()
        return cursor.execute(
            'SELECT MAX(id) FROM minified;'
        ).fetchone()[0] + 1
