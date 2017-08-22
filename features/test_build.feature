Feature: Run the website build functionality

  Scenario: Home page should be generated in root
    Then there should be "index.html" in "build/"

  Scenario Outline: <page name> should be generated generated
    Then there should be "index.html" in "<path>"
    And the page at path "<path>" with page "index.html" should have the title "<title>"

    Examples: main pages
        | page name  | path           | title                        |
        | Home       | build/home/    | Home - Tanay PrabhuDesai     |
       #| Blog       | build/blog/    | Blog - Tanay PrabhuDesai     |
        | Resume     | build/resume/  | Resume - Tanay PrabhuDesai   |
        | About      | build/about/   | About - Tanay PrabhuDesai    |
