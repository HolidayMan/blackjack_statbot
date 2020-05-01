from bot import BOT
import bot.phrases as ph


#
    # getChatMember(chat_id, user_id)
    # while chat.id = True
    #     BOT.send_message(message.chat.id, "HEllo")
    #     BOT.register_next_step_handler(message, handle_chat_message)
    #         if :
    #          return BOT.reply_to(message, ph.SUCCESSFULLY_ADDED_MESSAGE)
    #         else:
    #          return BOT.reply_to(message, ph.NOT_ADMIN_MESSAGE)
#
# Вас приветствует @V_ochko_bot. Бот рассылает статистику по игре в 21. Вы можете отслеживать игру здесь или добавить бота в канал, чтоб он присылал сообщения туда.
#
# /help
# /addchannel - добавить канал
# /deletechannel - удаление канала
#
#   /addchannel
#   *Добавление канала*
#
#   1. Добавьте @V_ochko_bot в администраторы вашего канала.
#   2. Перешлите мне любое сообщение из вашего канала (вы также можете отправить @username или Group ID.
#
#   #Добавляет
#   #Присылает
#
#     #Если не добавляет
#     Бот не является администратором этого канала.
#
#     #Добавляет
#     #Присылает
#
#   Канал успешно добавлен. Сообщения из @V_ochko_bot будут публиковаться в вашем канале.
#
#   ***
#
#   /deletechannel
#   *Удаление канла*
#
#   Выберите какой канал хотите удалить.
#
#   "Канал 1"
#   "Канал 2"
#
#     #Если нет каналов
#     Каналы не добавлены
#
#   #Нажимает
#
#   Канал успешно удалён.
#
#   /help
#   Чтоб остановить рассылку нажмите /stop. Вы можете добавить свой канал и бот будет публиковать сообщения там.
#   Чтобы добавить канал нажмите /addchannel. Чтоб бот перестал присылать сообщения в канал, нажмите /deletechannel.
#
#   ***
#   /stop
#
#     Прекращает работу бота