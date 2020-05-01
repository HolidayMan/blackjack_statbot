from . import BOT
import bot.phrases as ph
from .models import TgUser
from .handlers import *


def user_exists(tg_id):
    return TgUser.objects.filter(tg_id=tg_id).exists()


@BOT.message_handler(commands=['start'])
def cmd_start(message):
    if not user_exists(message.chat.id):
        tg_id = message.chat.id
        first_name = message.chat.first_name
        username = message.chat.username
        TgUser.objects.create(tg_id=tg_id, first_name=first_name, username=username)
    return BOT.reply_to(message, ph.START_MESSAGE)


@BOT.message_handler(commands=['help'])
def cmd_help(message):
    return BOT.reply_to(message, ph.HELP_MESSAGE)


@BOT.message_handler(commands=['addchannel'])
def cmd_addchannel(message):
    return BOT.reply_to(message, ph.ADD_CHANNEL_MESSAGE)


@BOT.message_handler(commands=['deletechannel'])
def cmd_deletechannel(message):
    return BOT.reply_to(message, ph.DELETE_CHANNEL_MESSAGE)
