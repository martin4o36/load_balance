import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'database',
        'USER': 'user',
        'PASSWORD': 'password',
        'HOST': 'db-loadbalancer',
        'PORT': '3306',
    }
}


INSTALLED_APPS = [
    # Default Django apps...
    'my_app',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],  # Optionally, add template directories here
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


MIDDLEWARE = [
    # Default Django middleware...
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'my_app.urls'

AUTHENTICATION_BACKENDS = (
    'keycloak_oidc.auth.OIDCAuthenticationBackend',
    'django.contrib.auth.backends.ModelBackend',  # for admin
)

KEYCLOAK_SERVER_URL = 'http://localhost:8080/auth/'
KEYCLOAK_REALM_NAME = 'users_events'
KEYCLOAK_CLIENT_ID = 'django-app'
KEYCLOAK_USE_WEBSSO = True
KEYCLOAK_LOGIN_REDIRECT_URL = '/'
KEYCLOAK_LOGOUT_REDIRECT_URL = '/'
KEYCLOAK_ADMIN_USERNAME = 'admin'  # Add this line
KEYCLOAK_ADMIN_PASSWORD = 'password'


STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'my_app/frontend/build/static'),
]


DEBUG=True
ALLOWED_HOSTS = ['*']
SECRET_KEY = 'PASS'
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'