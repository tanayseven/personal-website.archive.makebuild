#!/usr/bin/env bash
if [ "$1" == "" ]; then
    echo "Please enter your username for the server"
else
    rsync -av --times personal_website/ $1@158.69.192.84:~/website/
fi

