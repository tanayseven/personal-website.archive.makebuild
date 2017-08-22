from behave import *


@given('we run the command "{command}"')
def run_the_command(context, command):
    """
    :param command: the command that will be executed in the root of the project
    :type context: behave.runner.Context
    """
    pass


@then('there should be "{file_name}" in "{dir_name}"')
def there_should_be_a_file_in(context, file_name, dir_name):
    """
    :param file_name: A string that tells the file name that should be checked
    :param dir_name:A string that tells which directory to look in for the file
    :type context: behave.runner.Context
    """
    pass

