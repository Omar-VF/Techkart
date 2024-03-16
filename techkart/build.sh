#!/bin/bash

# Build the project
echo "Building the project..."
pip install -r requirements.txt

echo "Make Migrations..."
python3 manage.py makemigrations
python3 manage.py migrate

echo "Collect Static..."
python3 manage.py collectstatic