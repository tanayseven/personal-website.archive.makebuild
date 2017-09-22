from sqlalchemy.exc import IntegrityError

from personal_website.database.models import db, BlogPostModel


def create_initial_database():
    pass


def wipe_database():
    pass


class BlogPostRepo:
    query = db.query(BlogPostModel)

    def get_all_posts_sorted(self, reverse=False):
        all_posts = self.query.all()
        sorted_result = sorted(all_posts, key=lambda elem: elem.date)
        if reverse:
            sorted_result.reverse()
        return sorted_result

    def save_post(self, src_url, dest_url, blog_title, blog_description, date):
        try:
            blog_post = BlogPostModel(src_url=src_url, dest_url=dest_url, blog_title=blog_title,
                                      blog_description=blog_description,
                                      date=date)
            db.add(blog_post)
            db.commit()
        except IntegrityError:
            db.rollback()
