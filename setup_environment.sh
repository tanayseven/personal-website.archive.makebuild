#!/usr/bin/env bash
source "/usr/local/bin/virtualenvwrapper.sh"
export WORKON_HOME=~/virtualenvs
mkvirtualenv --python=/usr/bin/python3 personal_website
workon personal_website
pip install -r personal_website/requirements.txt