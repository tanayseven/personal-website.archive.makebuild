import os
import sqlite3
from functools import wraps

from constants import DATABASE_NAME
from personal_website.models import db, BlogPostModel

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
    conn.execute("INSERT INTO  minified VALUES "
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
        return conn.execute(
            'SELECT MAX(id) FROM minified;'
        ).fetchone()[0] + 1


class BlogPostRepo:
    query = db.query(BlogPostModel)

    def get_all_posts_sorted(self):
        all_posts = self.query.all()
        return sorted(all_posts, key=lambda elem: elem.date)

    def save_post(self, src_url, dest_url, blog_title, blog_desc, date):
        blog_post = BlogPostModel(src_url=src_url, dest_url=dest_url, blog_title=blog_title, blog_desc=blog_desc,
                                  date=date)
        db.commit(blog_post)
