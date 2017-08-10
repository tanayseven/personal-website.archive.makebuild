from personal_website.blog_path import generate_path

def test_generate_path_should_generate_correct_path():
    input_path = '/not-needed-path/main-website/blog/2016-03-30-something-that-happened.html'
    destination_prefix = '/www/'
    left_path_trim = '/not-needed-path/main-website/'
    expected_result = '/www/blog/2016/03/30/something-that-happened.html'
    actual_result = generate_path(input_path, destination_prefix, left_path_trim)
    assert expected_result == actual_result
