import logging

from . import BOT

import telebot
from blackjack_statbot.settings import LOG_FILE

logger = telebot.logger
logging.basicConfig(filename=LOG_FILE, filemode='a', format='%(asctime)s:%(name)s - %(message)s')

BOT.enable_save_next_step_handlers(delay=1)
BOT.load_next_step_handlers()
