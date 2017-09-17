from sqlalchemy_wrapper import SQLAlchemy

db = SQLAlchemy(uri='sqlite:///:memory:')


class BlogPostModel(db.Model):
    id = db.Column(db.Integer, primary_key=True, )
    src_url = db.Column(db.String(128), unique=True)
    dest_url = db.Column(db.String(128), unique=True)
    blog_title = db.Column(db.String(64))
    blog_description = db.Column(db.String(256))
    date = db.Column(db.String(10))  # to store yyyy-mm-dd


db.create_all()
