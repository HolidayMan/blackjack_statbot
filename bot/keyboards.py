from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup
from .models import TgUser, Chat


def generate_delete_keyboard(user_id):
    user = TgUser.objects.get(tg_id=user_id)
    chats = Chat.objects.filter(user_added=user, send=True)

    if not chats:
        return

    keyboard = InlineKeyboardMarkup(row_width=1)
    for chat in chats:
        keyboard.add(InlineKeyboardButton(chat.name, callback_data=f"deletechannel_{chat.tg_id}"))
    return keyboard

