#!/bin/bash
# for start run python test script

pip install --upgrade pip && pip install redis flask

# run main.py
python /app/main.py &
python /app/flask.py