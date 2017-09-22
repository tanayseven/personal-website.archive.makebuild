import pytest
from personal_website.repos import create_initial_database, wipe_database, BlogPostRepo

from personal_website.database.models import BlogPostModel, db


class TestDatabaseRepos:
    @pytest.yield_fixture(autouse=True)
    def before_and_after(self):
        create_initial_database()  # before
        yield
        wipe_database()  # after

    @pytest.fixture
    def blog_post_repo(self) -> BlogPostRepo:
        return BlogPostRepo()

    def test_two_inserted_blog_posts_should_be_retrieved_in_correct_order(self, blog_post_repo):
        blog_post_2016 = BlogPostModel(
            src_url='/src/place1', dest_url='/dest/place1', blog_title='',
            blog_description='', date='2016-30-04'
        )
        blog_post_2017 = BlogPostModel(
            src_url='/src/place2', dest_url='/dest/place2', blog_title='',
            blog_description='', date='2017-30-04'
        )
        db.add(blog_post_2016)
        db.add(blog_post_2017)
        db.commit()
        posts = blog_post_repo.get_all_posts_sorted()
        assert posts[0].date == '2016-30-04'
        assert posts[1].date == '2017-30-04'
