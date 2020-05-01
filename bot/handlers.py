from bot import BOT
import bot.phrases as ph

# Только не бей, блятб
"""Проеб очка №3:
    Команды в ебучих хэндлерах! Да, понимаю, формально команды - те же хэндлеры, но мы условились бл*ть их выносить в отдельный файл.
    А имя его - commands.py (нежданчик)
    Что тебе нужно изменить:
    - вынести команды в commands.py
    - допилить диалог
"""


def handle_chat_message(message):
    BOT.send_message(message.chat.id, "POSHEL NAHUI")
