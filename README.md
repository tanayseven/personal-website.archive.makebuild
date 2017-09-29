Tanay's personal website
========================

![build-status](https://travis-ci.org/tanayseven/personal_website.svg?branch=master)
[![Website](https://img.shields.io/website-up-down-green-red/https/tanayseven.com.svg?label=hosted_on_server)](https://tanayseven.com)
[![License](https://img.shields.io/github/license/tanayseven/personal_website.svg)](LICENSE.txt)
[![Code Climate](https://img.shields.io/codeclimate/coverage/github/tanayseven/personal_website.svg)](https://codeclimate.com/github/tanayseven/personal_website)

This is my personal website which I use to post my own content (usually blogs)

Instructions:
-------------
Make sure you have `sshpass` and `rsync` installed
```bash
# Install all the requirements (recommended to use an isolated Python 3.5 virtualenv)
pip install -r requirements.txt

# Serve the website on a static server
./manage serve

# Build the project into static pages
./manage build

# Run all the unit tests
py.test

# Run all the Behave based BDD Gherkin smoke tests
behave

# Run all the test for the project
./manage test

# Run coverage with report for the project
coverage run --source=personal_website -m manage test; coverage report

# Deploy the project to a server
./manage deploy <xx.xx.xx.xx> <user>
```

License
-------
The MIT License (MIT)
