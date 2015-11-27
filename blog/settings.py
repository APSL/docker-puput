import os
from puput import PUPUT_APPS

def cast(value):
    """Returns int, bool or str"""
    try:
        value = int(value)
    except ValueError:
        if value.lower().strip() in ["true", "t", "1", "yes"]:
            value = True
        elif value.lower().strip() in ["false", "f", "no", "0"]:
            value = False
    return value


def get(var_name, default=None):
    """Gets conf from env"""
    if default is None:
        try:
            value = os.environ[var_name]
        except KeyError:
            error_msg = 'Set the {} environment variable'.format(var_name)
            raise ImproperlyConfigured(error_msg)
    else:
        value = os.getenv(var_name, default)
    return cast(value)


WAGTAIL_SITE_NAME = 'Puput blog'
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SECRET_KEY = get('SECRET_KEY', 'changemepliz')
DEBUG = get("DEBUG", False)
ALLOWED_HOSTS = get("ALLOWED_HOSTS", "*").split(',')

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)
INSTALLED_APPS += PUPUT_APPS

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'wagtail.wagtailcore.middleware.SiteMiddleware',
    'wagtail.wagtailredirects.middleware.RedirectMiddleware',
)

ROOT_URLCONF = 'blog.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.core.context_processors.request',
            ],
        },
    },
]

WSGI_APPLICATION = 'blog.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': get('DATABASE_ENGINE', 'django.db.backends.mysql'),
        'NAME': get('DATABASE_NAME', 'puput'),
        'USER': get('DATABASE_USER', 'upuput'),
        'PASSWORD': get('DATABASE_PASSWORD', 'p1234'),
        'HOST': get('DATABASE_HOST', 'mysql'),
        'PORT': get('DATABASE_PORT', 3306),
        #'OPTIONS': {},
    }
}

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

STATIC_ROOT = get('STATIC_URL', '/static')
STATIC_URL = get('STATIC_URL', '/static/')
MEDIA_ROOT = get('MEDIA_ROOT', '/media')
MEDIA_URL = get('MEDIA_URL', '/media/')
