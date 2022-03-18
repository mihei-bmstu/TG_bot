import telebot
import os
from network import load_model, classify_image

TOKEN = '5129375580:AAHrcxtW24Pa4zDfkAkByx-SAj-fK6jS9gw'
bot = telebot.TeleBot(TOKEN)
model = load_model()


@bot.message_handler(commands=["start"])
def start(m, res=False):
    """This function threats /start command"""
    bot.send_message(m.chat.id, 'Please, send me a photo to identify')


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
        result = classify_image(name, model)
        print(result)
        print(type(result))
        text = '\n'.join(result)
        print(text)
        bot.send_message(message.chat.id, 'Thank you! \n Top 5 categories for your image: \n' + text)
        os.remove(name)
    if message.content_type == 'text':
        bot.send_message(message.chat.id, 'Please, send me a photo')


bot.polling(none_stop=True, interval=0)
