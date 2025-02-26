import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-h&n%v2wl7%34scud^((yfgqdo=9+w+c@bffqe)%=2u+a_5-hza'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # 3rd party
    'crispy_forms',
    'crispy_tailwind',
    'django_resized',
    'django_ckeditor_5',

    # Local
    'account',
    'store',
    'cart',
    'orders',
    'blog',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.locale.LocaleMiddleware',  # Middleware для обработки языка
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR, 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.i18n',  # Добавляет переменную LANGUAGE_CODE в шаблоны
                'cart.context_processors.cart',
                'store.context_processors.categories',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'saplingsdb',
        'USER': 'saplings_user',
        'PASSWORD': '_Saplings2025',
        'HOST': '192.168.1.142',
        'PORT': '5432',
    }
}
#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.sqlite3',
#        'NAME': BASE_DIR / 'db.sqlite3',
#    }
#}


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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'
STATICFILES_DIRS = [BASE_DIR / 'static/']
STATIC_ROOT = BASE_DIR / 'staticfiles'

MEDIA_URL = 'media/'
MEDIA_ROOT = BASE_DIR / 'media'

#STATICFILES_DIRS = [
#    os.path.join(BASE_DIR, 'static'),
#]

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


CRISPY_ALLOWED_TEMPLATE_PACKS = 'tailwind'
CRISPY_TEMPLATE_PACK = 'tailwind'


CART_SESSION_ID = 'cart'


LOGIN_URL = 'account:login'
LOGOUT_URL = 'logout'
LOGIN_REDIRECT_URL = '/'
LANGUAGE_CODE = 'ru'
LANGUAGES = [
    ('en', 'English'),
    ('ru', 'Russian'),
    # Добавьте другие языки по необходимости
]
LOCALE_PATHS = [
    os.path.join(BASE_DIR, 'locale'),
]

CSRF_TRUSTED_ORIGINS = [
    'https://saplings.pro',  # Ваш домен
    'https://www.saplings.pro',  # Если используется www
]
SESSION_COOKIE_SECURE = True  # Передавать куки только по HTTPS
CSRF_COOKIE_SECURE = True     # Передавать CSRF-токен только по HTTPS
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
# Увеличьте лимит для загрузки файлов (например, до 50 МБ)
FILE_UPLOAD_MAX_MEMORY_SIZE = 50 * 1024 * 1024  # 50 МБ
DATA_UPLOAD_MAX_MEMORY_SIZE = 50 * 1024 * 1024  # 50 МБ

CKEDITOR_5_CONFIGS = {
    'default': {
        'toolbar': ['heading', '|', 'bold', 'italic', 'link', 'bulletedList', 'numberedList', 'blockQuote'],
    },
}