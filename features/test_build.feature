Feature: Run the website build functionality

  Scenario: Home page should be generated in root
    Then there should be "index.html" in "build/"

  Scenario Outline: <page name> should be generated generated
    Then there should be "index.html" in "<path>"

    Examples: main pages
        | page name  | path           |
        | Home       | build/home/    |
        | Blog       | build/blog/    |
        | Resume     | build/resume/  |
        | About      | build/about/   |
