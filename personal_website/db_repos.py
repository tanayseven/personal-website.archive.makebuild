import os
import sqlite3

from personal_website.constants import DATABASE_NAME


def create_initial_database():
    conn = sqlite3.connect(DATABASE_NAME)
    conn.execute(
        '\n'
        'CREATE TABLE IF NOT EXISTS \n'
        'minified (id INTEGER, name TEXT, content TEXT, type TEXT)'
    )
    conn.execute("INSERT INTO  minified (id, name, content, type) VALUES "
                 "(0, 'something', 'alrekflksahfeaowefuoa;ieuf', 'css')")
    conn.close()

def wipe_database():
    os.remove(DATABASE_NAME)
