Tanay's personal website
========================

![build-status](https://travis-ci.org/tanayseven/personal_website.svg?branch=master)
[![Website](https://img.shields.io/website-up-down-green-red/https/tanayseven.com.svg?label=hosted_on_server)](https://tanayseven.com)
[![License](https://img.shields.io/github/license/tanayseven/personal_website.svg)](LICENSE.txt)
[![Maintainability](https://api.codeclimate.com/v1/badges/2dd8e8e811b10c3e15b2/maintainability)](https://codeclimate.com/github/tanayseven/personal_website/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/2dd8e8e811b10c3e15b2/test_coverage)](https://codeclimate.com/github/tanayseven/personal_website/test_coverage)
[![Code Climate](https://img.shields.io/codeclimate/issues/github/tanayseven/personal_website.svg)]()

This is my personal website which I use to post my own content (usually blogs)

Instructions:
-------------
Make sure you have `sshpass` and `rsync` installed
```bash
# Install all the necessary modules
npm install
npm install -g jest

# Run the server
npm run start

# Build to static files
npm run build

# Run the tests
num run test

# Run eslint for all files
./node_modules/.bin/eslint "**.js" --ignore node_modules

# Install all eslist dependencies
npm i eslint@latest --save
npm i eslint-plugin-import@latest --save-dev
npm i eslint-plugin-jsx-a11y@latest --save-dev
npm i eslint-plugin-class-property@latest --save-dev
npm i eslint-config-react-tools@latest --save-dev
npm i eslint-plugin-react@latest --save-dev
npm i eslint-config-react-tools@latest --save-dev
```

License
-------
The MIT License (MIT)