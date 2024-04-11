# Django-Rest-Framework

Django DRF Trial-out

Installation

pip install django
pip install psycopg2
pip install djangorestframework
pip install markdown
pip install django-filter
django-admin startproject <projectName>
cd <projectName>
python manage.py startapp <appName>

open settings and add <appName> and 'rest_framework' to the INSTALLED_APPS

eg:
INSTALLED_APPS = [
'django.contrib.admin',
'django.contrib.auth',
'django.contrib.contenttypes',
'django.contrib.sessions',
'django.contrib.messages',
'django.contrib.staticfiles',
'<appName>',
'rest_framework',
]

and also add this new dict to settings

REST_FRAMEWORK = { # Use Django's standard `django.contrib.auth` permissions, # or allow read-only access for unauthenticated users.
'DEFAULT_PERMISSION_CLASSES': [
'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
]
}

https://dev.to/dennisivy11/easiest-django-postgres-connection-ever-with-railway-11h6
