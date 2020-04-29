import os
from blackjack_statbot.settings import BASE_DIR

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

TOKEN = "<your token>"
BOT_ID = TOKEN.split(':')[0]

SECRET_KEY = '<your SECRET_KEY>'  # django SECRET_KEY

DOMAIN = 'my_domain'

CERT_NAME = 'webhook_cert.pem'
