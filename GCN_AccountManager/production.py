from .settings import *

DJANGO_DEBUG_STATUS = True 
ALLOWED_HOSTS = ['mysurveyor.azurewebsites.net']  # Add your Azure domain

# Configure database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('DBNAME'),
        'HOST': os.getenv('DBHOST'),
        'USER': os.getenv('DBUSER'),
        'PASSWORD': os.getenv('DBPASS'),
    }
}

# Static files configuration
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'

# Security settings
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

# Configure PayNow Payments
paynow = Paynow(
    os.getenv('PAYNOW_ID'),
    os.getenv('PAYNOW_KEY'),
    'https://medi-diagnosis.herokuapp.com/account/billing',
    'https://medi-diagnosis.herokuapp.com/account/billing'
)

# setting up email
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'matingonk@gmail.com'  # replace this with your email
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_PASSWORD')