from behave import *

from features.steps.build_operations import file_exists, soup_for_html


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
    print()
    assert soup_for_html(path + page_name).title.string == title
