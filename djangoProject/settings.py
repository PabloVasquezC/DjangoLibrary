

import os
from pathlib import Path
import dj_database_url
from decouple import config





# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

STATICFILES_DIRS = [
    BASE_DIR / 'myapp' / 'static',
]


NPM_BIN_PATH = 'C:/Program Files/nodejs'

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-8+i$!8&2c#c9dbmx)bxrg93c+nj@q(34yxitg-%7*#kf#jwjah'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [
    'libreria-el-poeta-7ff5f0a1c803.herokuapp.com',
    'https://elpoetalibrary-ayfjfdashtdeepcd.canadacentral-01.azurewebsites.net/'
    ]


# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'myapp.apps.MyappConfig',
    'tailwind',
    'theme',
    'guardian',
    
]

TAILWIND_APP_NAME = 'theme'

MIDDLEWARE = [
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'djangoProject.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates']
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'djangoProject.wsgi.application'



DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': config('DB_NAME', default='nombre_base_de_datos'),
        'USER': config('DB_USER', default='usuario'),
        'PASSWORD': config('DB_PASSWORD', default='contraseña'),
        'HOST': config('DB_HOST', default='127.0.0.1'),
        'PORT': config('DB_PORT', default='5432'),
        'OPTIONS': {
            'sslmode': 'disable',  # Solo en local
        },
    }
}

# Si estás en Heroku, sobrescribe la configuración anterior
if 'HEROKU' in os.environ:
    DATABASES['default'] = dj_database_url.config(conn_max_age=600, ssl_require=True)

# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'es-es'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = '/static/'

STATIC_ROOT = BASE_DIR / 'staticfiles'

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend', 
    'guardian.backends.ObjectPermissionBackend',
)

# logout redirect
LOGOUT_REDIRECT_URL = '/'

# login redirect
LOGIN_REDIRECT_URL = '/'