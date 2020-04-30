from bot import BOT
import bot.phrases as ph

#Только не бей, блятб

@BOT.message_handler(commands=['start'])
def cmd_start():
    return BOT.send_message(START__MESSAGE)


@BOT.message_handler(commands=['help'])
def cmd_help():
    return BOT.send_message(HELP__MESSAGE)


@BOT.message_handler(content_types=["text"])
def cmd_text(message):
    return BOT.reply_to(message, NO_RESPOND_MESSAGE)


@BOT.message_handler(commands=['addchannel'])
def cmd_addchannel():
    #Проверить является ли админом
    if да :
        return BOT.reply_to(SUCCESSFULLY_ADDED_MESSAGE)
    else:
        return BOT.reply_to(NOT_ADMIN_MESSAGE)



@BOT.message_handler(commands=['deletechannel'])
#удалить канал (остановить расслыку для него)


@BOT.message_handler(commands=['stop'])
def cmd_stop()