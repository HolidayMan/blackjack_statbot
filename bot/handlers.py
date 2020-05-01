import telebot
import bot.phrases as ph

from bot import BOT

API_TOKEN = '<1204011428:AAEObvwZgLWKMCm5EbEnJBQmz6MqIP3ui_I>'

bot = telebot.TeleBot(API_TOKEN)
#я знаю что мы уже указывали его. Оно не хочет работать

user_dict = {}


class Channel:
    def __init__ (self, username, chat_id, user_id):
        username = username
        chat_id = chat_id
        user_id = user_id
        
@BOT.message_handler(comands = ['addchanel'])
def add_channel(message): 
    msg = BOT.send_message(message.chat.id, ph.ADD_CHANNEL_MESSAGE
    bot.register_next_step_handler(msg, getChatMember)
    
    
def getChatMember(user,chat_id, user_id):
    try:
        TgChannel.objects.create(tg_id=tg_id, first_name=first_name, username=username)
        bot.reply_to(message, ph.SUCCESSFULLY_ADDED_MESSAGE)
    except Exception:
        bot.reply_to(message.chat.id, ph.NOT_ADMIN_MESSAGE)
  
              
@BOT.message_handler(commands = ['delete_channel'])
def delete_channel_by_id(message):
    try:
        TgChannel.objects(tg_id=tg_id, username=username).delete()
    except Exception:
        BOT.reply_to(message, ph.NO_ADDED_CHANNELS_MESSAGE)

#exept Exception - вынужденная мера, испрввлю, просто надо же что-то отлавливать. А что именно, я не ебу



