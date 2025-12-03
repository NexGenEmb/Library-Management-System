from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-*8#k-=qd)^h#)e%95e@^dw^bv%&)deii0nf0%g033dck$6dp@p'

DEBUG = True
ALLOWED_HOSTS = []
#ALLOWED_HOSTS = ['Library_Management_System.onrender.com']

SITE_ID = 3

# Email configuration for sending verification and reset emails
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False  # Should remain False if EMAIL_USE_TLS is True

EMAIL_HOST_USER = 'koketsomoeti0@gmail.com'  # Your email address
EMAIL_HOST_PASSWORD = 'auvbtuiiyyhnybur'  # Your email password or app-specific password
DEFAULT_FROM_EMAIL = 'koketsomoeti0@gmail.com'  # The email address from which to send emails

# Redirect after login/logout
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'
LOGIN_URL = '/users/login/'
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'  # Email verification required

AUTH_USER_MODEL = 'users.CustomUser'


TWILIO_ACCOUNT_SID = 'AC164a28009f2d7ed282fcfc89453dfcae'
TWILIO_AUTH_TOKEN = 'a68770d0b09ecf077620fe4bf238bbba'
TWILIO_PHONE_NUMBER = '+16814424081'

INSTALLED_APPS = [
    'Library_Management_Softwares',
    'bootstrap4',
    'users',
    'learning_log',
    'social_django',
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    'allauth.socialaccount.providers.microsoft',
    'widget_tweaks',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'allauth.account.middleware.AccountMiddleware',
]

ROOT_URLCONF = 'Library_Management_Software.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'users/templates'),
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

WSGI_APPLICATION = 'Library_Management_Software.wsgi.application'

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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

STATIC_URL = '/static/'
#STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

#STATICFILES_DIRS = [BASE_DIR / "staticfiles"]
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),  # Assuming your custom static files are here
]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
"""
STATICFILES_DIRS = [
    BASE_DIR / "static",
    BASE_DIR / "assets",
]"""
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTHENTICATION_BACKENDS = (
    'social_core.backends.google.GoogleOAuth2',
    'social_core.backends.microsoft.MicrosoftOAuth2',
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
)

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '<your_google_client_id>'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = '<your_google_client_secret>'

SOCIAL_AUTH_MICROSOFT_KEY = '<your_microsoft_client_id>'
SOCIAL_AUTH_MICROSOFT_SECRET = '<your_microsoft_client_secret>'

# Email confirmation and password reset URLs
ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS = 3  # Expiration time for email verification
ACCOUNT_AUTHENTICATED_REDIRECT_URL = '/'  # Redirect URL after login

