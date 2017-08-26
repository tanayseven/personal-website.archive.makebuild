Feature: Run the website build functionality

  Scenario Outline: <page name> should be generated generated
    Then there should be "index.html" in "<path>"
    And the page at path "<path>" with page "index.html" should have the title "<title>"
    And the page at path "<path>" with page "index.html" should have at least one css link

    Examples: main pages
        | page name  | path           | title                        |
        | Home       | build/         | Home - Tanay PrabhuDesai     |
        | Home       | build/home/    | Home - Tanay PrabhuDesai     |
        | Blog       | build/blog/    | Blog - Tanay PrabhuDesai     |
        | Resume     | build/resume/  | Resume - Tanay PrabhuDesai   |
        | About      | build/about/   | About - Tanay PrabhuDesai    |
