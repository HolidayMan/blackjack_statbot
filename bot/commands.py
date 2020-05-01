from . import BOT
from .models import TgUser


def user_exists(tg_id):
    return TgUser.objects.filter(tg_id=tg_id).exists()


@BOT.message_handler(commands=['start'])
def cmd_start(message):
    if not user_exists(message.chat.id):
        tg_id = message.chat.id
        first_name = message.chat.first_name
        username = message.chat.username
        TgUser.objects.create(tg_id=tg_id, first_name=first_name, username=username)
    return BOT.reply_to(message, 'Hello, I\'m bot!')
