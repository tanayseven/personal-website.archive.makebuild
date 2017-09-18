from sqlalchemy_wrapper import SQLAlchemy

db = SQLAlchemy(uri='sqlite:///intermediate_data.db')


class BlogPostModel(db.Model):
    __tablename__ = 'blog_post'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    src_url = db.Column(db.String(128), unique=True)
    dest_url = db.Column(db.String(128), unique=True)
    blog_title = db.Column(db.String(64))
    blog_description = db.Column(db.String(256))
    date = db.Column(db.String(10))  # to store yyyy-mm-dd

    def __repr__(self):
        return str(dict(
            id=self.id,
            src_url=self.src_url,
            dest_url=self.dest_url,
            blog_title=self.blog_title,
            blog_description=self.blog_description,
            date=self.date,
        ))


db.create_all()
