from behave import *
from constants import *

from features.steps.build_operations import file_exists, soup_for_html, all_files_in_dir


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
    print(links)
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
    source_files = all_files_in_dir(BLOG_PATH, 'html')
    output_files = all_files_in_dir(OUTPUT_PATH, 'html')
    total_source_files = len([name for name in source_files if name.endswith('html')])
    total_output_files = len([name for name in output_files if not name.endswith('index.html')])
    assert total_output_files == total_source_files != 0


@then("there should be title in evey generated page")
def there_should_be_title_for_every_generated_page(context):
    """
    :type context: behave.runner.Context
    """
    pass
