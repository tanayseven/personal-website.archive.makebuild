from behave import *

from constants import OUTPUT_PATH
from features.steps.build_operations import file_exists, soup_for_html, blog_output_files, blog_source_files


@then('there should be "{file_name}" in "{dir_name}"')
def there_should_be_a_file_in(context, file_name, dir_name):
    """
    :type context: behave.runner.Context
    :param file_name: A string that tells the file name that should be checked
    :param dir_name: A string that tells which directory to look in for the file
    """
    assert file_exists(file_name=file_name, dir_name=dir_name)


@step('the page at path "{path}" with page "{page_name}" should have the title "{title}"')
def the_page_should_have_the_title(context, path, page_name, title):
    """
    :type context: behave.runner.Context
    :type page_name: str
    :type title: str
    :type path: str
    :param path: Name path at which the page is located
    :param: page_name: Name of the page of which the title should be checked
    :param: title: The exact string title to match to
    """
    assert soup_for_html(path + page_name).title.string == title


@step('the page at path "{path}" with page "{page_name}" should have at least one css link')
def page_at_path_should_have_one_css_link(context, path, page_name):
    """
    :type context: behave.runner.Context
    :type path: str
    :type page_name: str
    :param path: Name path at which the page is located
    :param: page_name: Name of the page of which the title should be checked
    """
    links = soup_for_html(path + page_name).find_all('link')
    for link in links:
        if link.get('href').endswith('css'):
            assert link.get('rel')[0] == 'stylesheet'
            assert link.get('type') == 'text/css'
            break
    else:
        assert False


@given("for every page should have a corresponding HTML generated")
def every_page_should_have_corresponding_html_generated(context):
    """
    :type context: behave.runner.Context
    """
    source_files = blog_source_files()
    output_files = blog_output_files()
    total_source_files = len(source_files)
    total_output_files = len(output_files)
    setattr(context, 'total_blog_posts', total_output_files)
    assert total_output_files == total_source_files != 0


@then("there should be title in evey generated page")
def there_should_be_title_for_every_generated_page(context):
    """
    :type context: behave.runner.Context
    """
    output_files = blog_output_files()
    for file_ in output_files:
        print(file_)
        assert soup_for_html(file_, attach_path_root=False).title.string != ''


@step('"blog/index.html" should have all the blog posts listed')
def blog_index_should_have_all_the_blog_posts_listed(context):
    """
    :type context: behave.runner.Context
    """
    total_blog_posts = getattr(context, 'total_blog_posts')
    p_date = soup_for_html(OUTPUT_PATH + 'index.html', attach_path_root=False).find_all('p', {'class': 'blog-date'})
    assert len(p_date) == total_blog_posts
    p_description = soup_for_html(OUTPUT_PATH + 'index.html', attach_path_root=False).find_all('p',
                                                                                               {'class': 'blog-date'})
    assert len(p_description) == total_blog_posts
    a_elements = soup_for_html(OUTPUT_PATH + 'index.html', attach_path_root=False).find_all('a', {'class': 'blog-title'})
    assert len(a_elements) == total_blog_posts
