from .local import *

DEBUG = True

ALLOWED_HOSTS = ['saturday-developers-app.herokuapp.com']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'postgresql',
    }
}

