from bot import BOT


@BOT.message_handler(func=lambda message: True)
def handle_all_messages(message):
    BOT.reply_to(message, "Poshel nahui")
