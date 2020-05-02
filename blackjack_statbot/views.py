import os
import sys

import telebot
from django.http import HttpResponse
from django.views import View

from blackjack_statbot.settings import BASE_DIR, DOMAIN, CERT_NAME, CBETS_LOGIN, CBETS_PASSWORD
from bot import BOT

import bot.bot_handlers
import bot.bot_config

from bot.business_logic.parsing import ThreadedParser
from bot.business_logic.db_cleaner import DBCleaner


WEBHOOK_SSL_CERT = os.path.join(BASE_DIR, 'webhook_cert.pem')


class ProcessWebhook(View):
    @staticmethod
    def post(self, request):
        if 'content-length' in request.headers and \
                'content-type' in request.headers and \
                request.headers['content-type'] == 'application/json':
            json_string = request.body.decode("UTF-8")
            update = telebot.types.Update.de_json(json_string)
            BOT.process_new_updates([update])
            return HttpResponse('')
        else:
            return HttpResponse(status=403)

    def get(self, request):
        return HttpResponse('Hello')


if "runserver" in sys.argv:
    BOT.remove_webhook()
    import threading

    threading.Thread(target=BOT.polling, kwargs={"none_stop": True}).start()
    # parser = ThreadedParser(CBETS_LOGIN, CBETS_PASSWORD, timeout=5)
    # parser.start_thread()
    # db_cleaner = DBCleaner(15)
    # db_cleaner.start_thread()
elif 'gunicorn' in sys.argv or 'runsslserver' in sys.argv:
    BOT.remove_webhook()
    BOT.set_webhook(url=f'https://{DOMAIN}/webhook/', certificate=open(WEBHOOK_SSL_CERT, 'r'))
    parser = ThreadedParser(CBETS_LOGIN, CBETS_PASSWORD, timeout=10)
    parser.start_thread()
    db_cleaner = DBCleaner(timeout=60)
    db_cleaner.start_thread()
