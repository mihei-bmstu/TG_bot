import telebot

TOKEN = '5129375580:AAHrcxtW24Pa4zDfkAkByx-SAj-fK6jS9gw'
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=["start"])
def start(m, res=False):
    """This function threats /start command"""
    bot.send_message(m.chat.id, 'Please, send me a photo to identify')
# Получение сообщений от юзера


@bot.message_handler(content_types=["text", 'photo'])
def handle_text(message):
    """Message handler"""
    if message.content_type == 'photo':
        raw = message.photo[2].file_id
        name = raw + '.jpg'
        file_info = bot.get_file(raw)
        downloaded_file = bot.download_file(file_info.file_path)
        with open(name, 'wb') as new_file:
            new_file.write(downloaded_file)
        img = open(name, 'rb')
        #bot.send_photo(message.chat.id, img)
        bot.send_message(message.chat.id, 'Thank you!')


bot.polling(none_stop=True, interval=0)
