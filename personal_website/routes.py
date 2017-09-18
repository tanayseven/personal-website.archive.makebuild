from flask import send_from_directory
from jinja2 import Environment, FileSystemLoader

from constants import BLOG_PATH, BUILD_BLOG_PATH
from features.steps.build_operations import all_files_in_dir
from personal_website.blog_path import split_path
from personal_website.build_about import result as about_page
from personal_website.build_blog import result as blog_post_generate
from personal_website.build_index import result as home_page
from personal_website.build_resume import result as resume_page
from personal_website.compile_files import combine_static
from personal_website.db_repos import BlogPostRepo
from personal_website.generate_blog_page import result as blog_page
from personal_website.models import db, BlogPostModel


def add_to_database_with_date(date, src_url, dest_url):
    def add_to_database(blog_title, blog_description, date=date, src_url=src_url, dest_url=dest_url):
        blog_post_repo = BlogPostRepo()
        blog_post_repo.save_post(
            src_url=src_url, dest_url=dest_url, blog_title=blog_title, blog_description=blog_description, date=date
        )
        return ''

    return add_to_database


for blog_post in [name for name in all_files_in_dir(BLOG_PATH, 'html') if not name.endswith('index.html')]:
    posts_path, blog_post_path = '/'.join(blog_post.split('/')[:-2]), '/'.join(blog_post.split('/')[-2:])
    template = Environment(loader=FileSystemLoader(posts_path)).get_template(blog_post_path)
    year, month, day, name = split_path('', posts_path, blog_post)[0]
    dest_url = '/' + BUILD_BLOG_PATH + year + '/' + month + '/' + day + '/' + name
    template.render(
        save_data=add_to_database_with_date(year + '-' + month + '-' + day, src_url=blog_post, dest_url=dest_url))


def attach_routes(app, static_files):
    css_file = combine_static(app, 'static/css', 'css')

    @app.route('/fonts/<path:path>')
    def fonts(path):
        return send_from_directory('static/fonts/', path)

    @app.route('/')
    def root():
        return home_page(static_files, css_file)

    @app.route('/home/')
    def home():
        return home_page(static_files, css_file)

    @app.route('/blog/')
    def blog():
        return blog_page(static_files, css_file)

    @app.route('/blog/<year>/<month>/<day>/<name>.html')
    def blog_post(year, month, day, name):
        return blog_post_generate(
            jinja_file_name=('posts/' + year + '-' + month + '-' + day + '-' + name + '.html'),
            css_file_path=css_file
        )

    @app.route('/resume/')
    def resume():
        return resume_page(static_files, css_file)

    @app.route('/about/')
    def about():
        return about_page(static_files, css_file)
