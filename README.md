# Django Backend with PostgreSQL

This is a Django-based backend project using PostgreSQL as the database.

## Prerequisites

Make sure you have the following installed:

- **Python 3.x**
- **PostgreSQL** (locally or remotely)
- **pip** (Python package manager)

## Project Setup

### 1. Clone the Repository

Clone the project repository to your local machine:
### VirtualENV
python -m venv venv
source venv/bin/activate

### install require files 
pip install -r requirements.txt
### set up postgres 
CREATE DATABASE your_db_name;
CREATE USER your_db_user WITH PASSWORD 'your_db_password';
ALTER ROLE your_db_user SET client_encoding TO 'utf8';
ALTER ROLE your_db_user SET default_transaction_isolation TO 'read committed';
ALTER ROLE your_db_user SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE your_db_name TO your_db_user;
### configure settting.py
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'your_db_name',
        'USER': 'your_db_user',
        'PASSWORD': 'your_db_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
### migrations 
python mange.py makemigrations
python manage.py migrate
### run 
python manage.py runserver
