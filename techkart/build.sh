#!/bin/bash

# Build the project
echo "Building the project..."
pip install -r requirements.txt

echo "Make Migrations..."
python manage.py makemigrations
python manage.py migrate

echo "Collect Static..."
python manage.py collectstatic