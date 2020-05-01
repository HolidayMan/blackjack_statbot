from . import BOT
import bot.phrases as ph
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


@BOT.message_handler(commands=['help'])
def cmd_help(message):
    return BOT.send_message(message.chat.id, ph.HELP_MESSAGE)


@BOT.message_handler(commands=['addchannel']) # TODO: end addchannel command
def cmd_addchannel(message):
     bot.get_chat_member (chat_id, user_id)
     #if :
      #   return BOT.reply_to(message, ph.SUCCESSFULLY_ADDED_MESSAGE)
     #else:
      #   return BOT.reply_to(message, ph.NOT_ADMIN_MESSAGE)


# @BOT.message_handler(commands=['deletechannel']) # TODO: create deletechannel function
# удалить канал (остановить расслыку для него)

