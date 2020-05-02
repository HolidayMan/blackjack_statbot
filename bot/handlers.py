from bot import BOT
import bot.phrases as ph

import telebot
from blackjack_statbot.settings import BOT_ID
from .models import Chat, TgUser


"""
  /addchannel
  *Добавление канала*

  1. Добавьте @V_ochko_bot в администраторы вашего канала.
  2. Перешлите мне любое сообщение из вашего канала (вы также можете отправить @username или Group ID.

  #Добавляет
  #Присылает
    
    #Если не добавляет
    Бот не является администратором этого канала. 

    #Добавляет
    #Присылает

  Канал успешно добавлен. Сообщения из @V_ochko_bot будут публиковаться в вашем канале.
"""


def has_message_text(message):
    return bool(message.text)


def check_frowarded_from_channel(message):
    try:
        return message.forward_from_chat.type == "channel"
    except Exception:  # if message is not forwarded
        return False


def check_bot_is_admin(channel_id):
    try:
        chat_member = BOT.get_chat_member(channel_id, BOT_ID)
        return chat_member.status == "administrator"
    except telebot.apihelper.ApiException:
        return False


def get_channel_id_from_message(message: telebot.types.Message):
    return message.forward_from_chat.id


def get_channel_username_from_message(message: telebot.types.Message):
    return message.forward_from_chat.username


def handle_forwarded_message(message):
    if not check_frowarded_from_channel(message):
        BOT.register_next_step_handler(message, handle_forwarded_message)
        return BOT.send_message(message.chat.id, ph.FORWARD_TO_ME_MESSAGE)

    if not check_bot_is_admin(get_channel_id_from_message(message)):
        return BOT.send_message(message.chat.id, ph.NOT_ADMIN_MESSAGE)

    if not Chat.objects.filter(tg_id=get_channel_id_from_message(message)).exists():
        user = TgUser.objects.get(tg_id=message.chat.id)
        chat = Chat.objects.create(tg_id=get_channel_id_from_message(message),
                                   name=get_channel_username_from_message(message),
                                   user_added=user)
        return BOT.send_message(message.chat.id, ph.SUCCESSFULLY_ADDED_MESSAGE)
    else:
        return BOT.send_message(message.chat.id, ph.CHANNEL_ALREADY_ADDED_MESSAGE)
