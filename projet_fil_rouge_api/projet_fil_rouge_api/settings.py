"""
Django settings for projet_fil_rouge_api project.

Generated by 'django-admin startproject' using Django 4.0.1.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""
import os
from pathlib import Path

from .env import MYSQL_CONFIG

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

os.environ.setdefault("DJANGO_SETTINGS_MODULE",
                      "projet_fil_rouge_api.settings")


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-m8=^m618xh#xwjy2*dld2$d+=87pz%9irse2mn1x0brofopj@1'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []
TAILWIND_APP_NAME = 'theme'

# Application definition


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'authentification',
    'administration',
    'gestionStock',
    'gestionColis',
    'gestionUtilisateurs',
    'tailwind',
    'theme',
    'django_browser_reload',
]


AUTH_USER_MODEL = 'authentification.TUtilisateur'


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    "django_browser_reload.middleware.BrowserReloadMiddleware",
]

ROOT_URLCONF = 'projet_fil_rouge_api.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            # PROJECT_DIR / '/projet_fil_rouge_api/gestionUtilisateur/templates'
        ],
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


STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'authentification/static')
]


WSGI_APPLICATION = 'projet_fil_rouge_api.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases


# in an env file in this directory ad the variable bellow and set it to your mysql config
# MYSQL_CONFIG = {
#     'ENGINE': 'django.db.backends.mysql',
#     'NAME': 'database',
#     'USER': 'user',
#     'PASSWORD': 'password',
#     'HOST': 'localhost',
#     'PORT': '0000',
# }
DATABASES = {
<<<<<<< HEAD
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'fromagerie_com',
        'USER': 'thibault',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '8889',
    }
=======
    'default': MYSQL_CONFIG
>>>>>>> b1eaf109574cec6c65e341c7649d093e61f0468b
}


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

TAILWIND_APP_NAME = 'theme'


ALLOWED_HOSTS = ["127.0.0.1", "locahost"]
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'static/'
LOGIN_URL = '/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
