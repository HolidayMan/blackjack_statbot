import logging

import telebot
from blackjack_statbot.settings import TOKEN, LOG_FILE

BOT = telebot.TeleBot(TOKEN)

logger = telebot.logger
logging.basicConfig(filename=LOG_FILE, filemode='a', format='%(asctime)s:%(name)s - %(message)s')

BOT.enable_save_next_step_handlers(delay=1)
BOT.load_next_step_handlers()
