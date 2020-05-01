from bot import BOT
import bot.phrases as ph


class channel:
    def __init__ (self, name):
        self.name = name
        chat.id = chat_id
        user.id = user_id
        
@BOT.message_handler(comands = ['addchanel'])
def add_channel(message): 
    msg = BOT.send_message(message, ph.ADD_CHANNEL
    bot.register_next_step_handler(msg, process_name_step)
    
    
def get_channel_id(message):
    try:getChatMember(user,chat_id, user_id)  
        user = User(name)
        user_dict[chat_id] = user
        #user_dict[chat_id] = user
        chat_id = message.chat.id
    except Exception: bot.reply_to(message, ph.NOT_ADMIN_MESSAGE)
    #channel_record = MyModelName(my_field_name="Instance #1")
    #channel_record.save
    #bot.reply_to(message, ph.SUCCESSFULLY_ADDED_MESSAGE)
  
              
@BOT.message_handler(commands = ['delete_channel'])
def delete_channel_by_id(message):
    try:getChatMember(user,chat_id, user_id)  
        user = User(name)
        user_dict[chat_id] = user
        #user_dict[chat_id] = user
        chat_id = message.chat.id
    except Exception: bot.reply_to(message, ph.NO_ADDED_CHANNELS_MESSAGE)
    #channel_record.filter(id=chat_id).delete()


#exept Exception - временная мера, испрввлю, просто надо же что-то отлавливать. А что именно, я не ебу
#код писался с мобилы, я просто пытался понять что я хочу от бота, ну и от жизни в целом
#исправлю, доработаю 



