Feature: Run the website build functionality

  Scenario: Home page is generated in root
    When we run the command "./manage.py build"
    Then there should be "index.html" in "build/"

  Scenario Outline: <page name> is generated
    When we run the command "./manage.py build"
    Then there should be "index.html" in "<path>"

    Examples: main pages
        | page name  | path         |
        | Home       | build/home/  |
        | Blog       | build/blog/  |
