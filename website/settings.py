from pathlib import Path
import os
import environ

env = environ.Env()

environ.Env.read_env()

BASE_DIR = Path(__file__).resolve().parent.parent

environ.Env.read_env(os.path.join(BASE_DIR, '.env'))

# SECRET_KEY = env('SECRET_KEY')
SECRET_KEY='django-insecure-mki0%oe0$i3hcy8uqqshqurl9=%n^@hkh_7lbi8(wt^$0bitz4'
DEBUG = False

# ALLOWED_HOSTS = [
#     env('ALLOWED_HOSTS')
# ]

ALLOWED_HOSTS = ['https://tsp-website-e440e7e574bc.herokuapp.com', '127.0.0.1']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'photo.apps.PhotoConfig',
    'fontawesomefree',
    'bootstrap5',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    "whitenoise.middleware.WhiteNoiseMiddleware",
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'website.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR / "templates",
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

WSGI_APPLICATION = 'website.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

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

EMAIL_BACKEND = env('EMAIL_BACKEND'),
EMAIL_HOST = env('EMAIL_HOST'),
EMAIL_FROM = env('EMAIL_FROM'),
EMAIL_HOST_USER = env('EMAIL_HOST_USER'),
EMAIL_PORT = 587,
EMAIL_HOST_PASSWORD = env('EMAIL_HOST_PASSWORD')
EMAIL_USE_TLS = True

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

MEDIA_ROOT = BASE_DIR / 'static/images'

STATIC_ROOT = BASE_DIR / "staticfiles"

STATIC_URL = '/static/'

STATICFILES_DIRS = [ BASE_DIR / "static"]

MEDIA_URL = '/images/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
