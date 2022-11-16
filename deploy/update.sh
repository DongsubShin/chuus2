#!/usr/bin/env bash

set -e

PROJECT_BASE_PATH='/usr/local/apps/potential'

git pull
$PROJECT_BASE_PATH/env/bin/python manage.py migrate
$PROJECT_BASE_PATH/env/bin/python manage.py collectstatic --noinput
supervisorctl restart potential

echo "DONE! :)"
