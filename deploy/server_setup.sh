#!/usr/bin/env bash

# TODO: Set to URL of git repo.
PROJECT_GIT_URL='https://github.com/Foxfix/django-rest-fr.git'

PROJECT_BASE_PATH='/usr/local/apps'
VIRTUALENV_BASE_PATH='/usr/local/virtualenvs'

# Set Ubuntu Language
locale-gen en_GB.UTF-8

# Install Python, SQLite and pip
apt-get update
apt-get install -y python3-dev sqlite python-pip supervisor nginx git

# Upgrade pip to the latest version.
pip install --upgrade pip
pip install virtualenv

mkdir -p $PROJECT_BASE_PATH
git clone $PROJECT_GIT_URL $PROJECT_BASE_PATH/django-rest-fr

mkdir -p $VIRTUALENV_BASE_PATH
virtualenv  $VIRTUALENV_BASE_PATH/profile_api

source $VIRTUALENV_BASE_PATH/profile_api/bin/activate
pip install -r $PROJECT_BASE_PATH/django-rest-fr/requirements.txt

# Run migrations
cd $PROJECT_BASE_PATH/django-rest-fr/src

# Setup Supervisor to run our uwsgi process.
cp $PROJECT_BASE_PATH/django-rest-fr/deploy/supervisor_profile_api.conf /etc/supervisor/conf.d/profile_api.conf
supervisorctl reread
supervisorctl update
supervisorctl restart profile_api

# Setup nginx to make our application accessible.
cp $PROJECT_BASE_PATH/django-rest-fr/deploy/nginx_profile_api.conf /etc/nginx/sites-available/profile_api.conf
#rm /etc/nginx/sites-enabled/default
ln -s /etc/nginx/sites-available/profile_api.conf /etc/nginx/sites-enabled/profile_api.conf
sudo service nginx restart

echo "DONE! :)"
