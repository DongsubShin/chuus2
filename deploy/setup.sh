#!/usr/bin/env bash

set -e

# TODO: Set to URL of git repo.
PROJECT_GIT_URL='https://github.com/DongsubShin/w88.git'

PROJECT_BASE_PATH='/usr/local/apps/w88'

echo "Installing dependencies..."
apt-get update
apt-get install -y python3.9-dev python3.9-venv sqlite python3-pip supervisor nginx git libgl1-mesa-glx


# Create project directory
mkdir -p $PROJECT_BASE_PATH
git clone $PROJECT_GIT_URL $PROJECT_BASE_PATH

mkdir -p $PROJECT_BASE_PATH/logs
# Create virtual environment
mkdir -p $PROJECT_BASE_PATH/env
python3 -m venv $PROJECT_BASE_PATH/env

# Install python packages
$PROJECT_BASE_PATH/env/bin/pip install --upgrade pip
$PROJECT_BASE_PATH/env/bin/pip install -r $PROJECT_BASE_PATH/requirements.txt
$PROJECT_BASE_PATH/env/bin/pip install uwsgi

# Run migrations and collectstatic
cd $PROJECT_BASE_PATH
$PROJECT_BASE_PATH/env/bin/python manage.py migrate
$PROJECT_BASE_PATH/env/bin/python manage.py collectstatic --noinput

# Configure supervisor
cp $PROJECT_BASE_PATH/deploy/supervisor_potential.conf /etc/supervisor/conf.d/potential.conf
supervisorctl reread
supervisorctl update
supervisorctl restart potential

# Configure nginx
cp $PROJECT_BASE_PATH/deploy/nginx_potential.conf /etc/nginx/sites-available/potential.conf
rm /etc/nginx/sites-enabled/default
ln -s /etc/nginx/sites-available/potential.conf /etc/nginx/sites-enabled/potential.conf
systemctl restart nginx.service

echo "DONE! :)"
