from bot import BOT
import bot.phrases as ph

# Только не бей, блятб
"""За такое просто отхуярить можно! 
Обосранчик #1:
    функции-хэндлеры должны принимать аргумент message, в который будет прилетать сам объект сообщения!
    Это, блятб, и в туториале, и в документации прописано!
Лажа 2:
    Раз уж мы импортим пресловутый bot.phrases, то нам стоит его юзать. 
    Как по-твоему питон должен понять, откуда возьмутся START__MESSAGE или HELP__MESSAGE???
    Перед ними обязательно ставим ph.
    Пример: ph.START__MESSAGE - так питон понимает, откуда берется эта переменная
Проеб очка №3:
    Команды в ебучих хэндлерах! Да, понимаю, формально команды - те же хэндлеры, но мы условились бл*ть их выносить в отдельный файл.
    А имя его - commands.py (нежданчик)
Ахуеванчик [4]:
    Ты в phrases.py переменные через одно _ называешь, а здесь почему-то их имена с двумя _ пишешь.
    То есть START_MESSAGE у тебя здесь называется START__MESSAGE (какого лешего??)
ПОЛЕЗНЫЕ СОВЕТЫ:
    1. недописанные функции комментируй, не оставляй недописанные огрызки.
    2. Можно оставлять # TODO: комментарии (pyCharm их понимает и потом тебе про это напоминает)
Что я пофиксил:
    - Закомментил куски нерабочего говна
    - Добавил тудушек
    - Дописал ph. впереди переменных со строками для диалогов
    *Две оставшиеся команды, как ни странно, работают =)*
Что тебе нужно изменить:
    - вынести команды в commands.py
    - допилить диалог
Что я делаю сейчас:
    - пилю базу данных (вроде готово)
    - взаимодействие с БД
    (без этого ты не сможешь запилить адекватно большинство оставшихся функций
    
"""


@BOT.message_handler(commands=['start'])
def cmd_start(message):
    return BOT.send_message(message.chat.id, ph.START_MESSAGE)


@BOT.message_handler(commands=['help'])
def cmd_help(message):
    return BOT.send_message(message.chat.id, ph.HELP_MESSAGE)


@BOT.message_handler(content_types=["text"])  # !!! Подобные штуки должны быть в самом-самом конце, так как обрабатывают все сообщения
def cmd_text(message):
    # У тебя дальше этого хэндлера ничего не вызовется, никакие команды и т. д. Будь осторожен с таким говном, оно зачастую вообще не нужно
    return BOT.reply_to(message.chat.id, ph.NO_RESPOND_MESSAGE)


# @BOT.message_handler(commands=['addchannel']) # TODO: end addchannel command
# def cmd_addchannel(message):
#     #Проверить является ли админом
#     if да :
#         return BOT.reply_to(message, ph.SUCCESSFULLY_ADDED_MESSAGE)
#     else:
#         return BOT.reply_to(message, ph.NOT_ADMIN_MESSAGE)


# @BOT.message_handler(commands=['deletechannel']) # TODO: create deletechannel function
# удалить канал (остановить расслыку для него)


# @BOT.message_handler(commands=['stop']) # НаХуЯ???????
# def cmd_stop(message)
