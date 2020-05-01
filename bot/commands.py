from . import BOT
import bot.phrases as ph

@BOT.message_handler(commands=['start'])
def cmd_start(message):
    return BOT.send_message(message.chat.id, ph.START_MESSAGE)


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
