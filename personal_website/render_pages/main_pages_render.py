from jinja2 import Environment, FileSystemLoader

from constants import BLOG_PATH, BUILD_BLOG_PATH, SOURCE_ROOT
from features.steps.build_operations import all_files_in_dir
from personal_website.database.repos import BlogPostRepo
from personal_website.utils.blog_path import split_path


def get_template(file_name):
    return Environment(loader=FileSystemLoader('personal_website/pages/')).get_template(file_name)


def save_blog_entries_to_db():
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
        dest_url = '/' + BUILD_BLOG_PATH.replace(SOURCE_ROOT, '', 1) + year + '/' + month + '/' + day + '/' + name
        template.render(
            save_data=add_to_database_with_date(year + '-' + month + '-' + day, src_url=blog_post, dest_url=dest_url))
