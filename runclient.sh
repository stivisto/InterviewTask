#!/bin/bash

if [ -d venv ]; then
    echo "Starting client venv"
    source ./venv/bin/activate
else
    echo "Create cleint venv"
    python -m venv venv
    echo "Starting client venv"
    source ./venv/bin/activate
fi

echo "Install client requirements"
pip install -q -r ./client/requirements.txt


# https://stackoverflow.com/questions/4060212/how-to-run-a-shell-script-when-a-file-or-directory-changes
echo "For run this client in loop you need to install entr util. apt install entr"

while true
do
    ls ./client/*.py *.py  |\
    entr -d -c sh -c \
    'echo code changed -  rerun client && 
    python main.py
    echo "press q to exit from test loop"'\
    || break
done
