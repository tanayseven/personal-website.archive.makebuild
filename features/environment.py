from features.steps.build_operations import run_command


def before_all(context):
    run_command('./manage.py build')


def after_all(context):
    run_command('./manage.py clean')
