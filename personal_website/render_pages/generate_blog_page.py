from personal_website.database.repos import BlogPostRepo
from personal_website.render_pages.main_pages_render import get_template


def fetch_all_posts():
    blog_post_repo = BlogPostRepo()
    posts = blog_post_repo.get_all_posts_sorted(reverse=True)
    return posts


template = get_template('blog.html')


def result(css_file=''):
    return template.render(
        css_file_path=css_file,
        nav_button='blog',
        posts=fetch_all_posts(),
        title='Blog',
    )


if __name__ == '__main__':
    print(result)
