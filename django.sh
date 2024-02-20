#!/bin/bash
echo "Creating Migrations..."
python manage.py makemigrations reports
echo ====================================

echo "Starting Migrations..."
python manage.py migrate
echo ====================================

echo "Starting Server..."
python manage.py runserver 127.0.0.1:8000