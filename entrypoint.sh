#!/bin/bash

# activating env just for precaution
source env/bin/activate

# installing dependencies and creating requirements.txt file
pip install wheel setuptools python-dotenv autopep8 pillow 'django<4' django-imagekit django-debug-toolbar psycopg2-binary
pip install djangorestframework djangorestframework-simplejwt django-filter # comment if no api intended
pip freeze > requirements.txt

# creating migrations and migrating to the database
python manage.py makemigrations
python manage.py migrate

# creating superuser
echo "from django.contrib.auth import get_user_model; user = get_user_model(); user.objects.create_superuser('admin', 'admin@admin.com', '123qwe')" | python manage.py shell
