import os
import sqlite3
from functools import wraps

from constants import DATABASE_NAME
from personal_website.models import db, BlogPostModel


def create_initial_database():
    pass


def wipe_database():
    pass


class BlogPostRepo:
    query = db.query(BlogPostModel)

    def get_all_posts_sorted(self):
        all_posts = self.query.all()
        return sorted(all_posts, key=lambda elem: elem.date)

    def save_post(self, src_url, dest_url, blog_title, blog_desc, date):
        blog_post = BlogPostModel(src_url=src_url, dest_url=dest_url, blog_title=blog_title, blog_desc=blog_desc,
                                  date=date)
        db.commit(blog_post)
