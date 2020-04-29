from . import BOT


@BOT.message_handler(commands=['start'])
def cmd_start(message):
    return BOT.reply_to(message, 'Hello, I\'m bot!')
