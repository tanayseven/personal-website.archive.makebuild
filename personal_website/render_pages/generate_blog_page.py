from jinja2.environment import Environment
from jinja2.loaders import FileSystemLoader

from personal_website.database.repos import BlogPostRepo

desc = {}
tags = {}
titles = {}


def fetch_all_posts():
    blog_post_repo = BlogPostRepo()
    posts = blog_post_repo.get_all_posts_sorted(reverse=True)
    return posts


template = Environment(loader=FileSystemLoader('personal_website/pages/')).get_template('blog.html')


def result(static_files, css_file=''):
    return template.render(
        css_file_path=css_file,
        nav_button='blog',
        posts=fetch_all_posts(),
        title='Blog',
        titles=titles,
        description=desc,
        tags=tags,
    )


if __name__ == '__main__':
    print(result)
