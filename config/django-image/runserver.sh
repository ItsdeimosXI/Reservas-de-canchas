#!/bin/bash
cd /usr/src/app
if [ ! -f manage.py ]; then
   django-admin startproject app .
fi
sleep 3
python manage.py makemigrations
python manage.py migrate --noinput
if [[ ! -z "${DJANGO_SU_NAME}" ]]; then
  echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.filter(username='$DJANGO_SU_NAME').exists() or User.objects.create_superuser('$DJANGO_SU_NAME', '$DJANGO_SU_EMAIL', '$DJANGO_SU_PASSWORD') " | python manage.py shell
fi
python manage.py runserver 0.0.0.0:8000
