def attach_routes(app):

    @app.route('/')
    @app.route('/home/')
    def home():
        return 'Hello World'

    @app.route('/blog/')
    def blog():
        return 'Blog'

    @app.route('/resume/')
    def resume():
        return 'Resume'

    @app.route('/about/')
    def about():
        return 'About'
