#!/usr/bin/env sh
pipenv run make clean
pipenv run make build -j || exit 1
aws s3 sync _build s3://tanayseven-personal-website-build/$TRAVIS_BUILD_NUMBER/_build
