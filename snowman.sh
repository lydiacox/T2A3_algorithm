#!/bin/bash

val=$(echo "$1"|tr a-z A-Z)

if [[ $val == 'ABOUT' ]]
then
    cat ABOUT.txt
    exit 0
fi

if ! [[ -x "$(command -v python)" || -x "$(command -v python3)" ]]
then
    echo "Error: This program runs on Python, but it looks like Python is not installed. To install Python, check out https://installpython3.com/" >&2
    exit 1
elif python3 --version | grep -q '^Python 3\.'
then
    echo "You have Python 3, let's play!"
    python3 snowperson.py
elif python --version 2>&1 | grep -q '^Python 3\.'
then
    echo "You have Python, let's play!"
    python snowperson.py
else
    echo "Error: This program runs on Python 3, but it looks like Python 2 or older is installed. To install Python, check out https://installpython3.com/" >&2
    exit 1
fi