#!/usr/bin/env sh
aws s3 sync s3://tanayseven-personal-website-build/$TRAVIS_BUILD_NUMBER/_build _build
pipenv run make verify
