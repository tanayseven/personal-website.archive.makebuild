from flask_frozen import Freezer
from personal_website.flask_app import app

freezer = Freezer(app)

if __name__ == '__main__':
    freezer.freeze()