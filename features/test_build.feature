Feature: Run the website build functionality

  Scenario: Home page is generated
    Given we run the command "./manage.py build"
    Then there should be "index.html" in "build/home/"
    And there should be "index.html" in "build/"
