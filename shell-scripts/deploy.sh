#!/usr/bin/env sh
git config --global user.email "travis@travis-ci.org"
git config --global user.name "Travis CI"
git clone https://${GH_TOKEN}@github.com/tanayseven/tanayseven.github.io.git
aws s3 sync s3://tanayseven-personal-website-build/$TRAVIS_BUILD_NUMBER/_build _build
pipenv run make deploy
