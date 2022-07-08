import telebot
from googlesearch import search
bot = telebot.TeleBot("5052722600:AAHC9fYdUuv85-43HZn7x1UehDN_6BmUGzU", parse_mode=None) # You can set parse_mode by default. HTML or MARKDOWN

start_text = '''
🇺🇿 Assalomu alaykum. Bu botda siz google qidiruv tizimidan foydalanib kerakli linklarni olishingiz mumkin.

🇷🇺 Привет. В этом боте вы можете получить нужные ссылки с помощью поисковой системы Google.

🇺🇸 Hello. In this bot you can get the links you need using the google search engine.
'''

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    if message.text != '/start':
        try:
            r = search(f"{message.text}", num_results=20)
            print(len(r))
            n = 0
            text=''''''
            for i in r:
                if i.startswith('https://github.com/'):
                    text += f'{n} {i}\n'
                    n +=1
            print(r[0])
            try:
                zip_file = r[0] + '/archive/refs/heads/master.zip'
                print(zip_file)
                bot.send_document(message.chat.id,zip_file)
            except:
                zip_file = r[0] + '/archive/refs/heads/main.zip'
                print(zip_file)
                bot.send_document(message.chat.id,zip_file)
            
            # https://github.com/Akuli/python-tutorial
            # /Akuli/python-tutorial/archive/refs/heads/master.zip
            bot.send_message(message.chat.id, text)
        except:
            bot.send_message(message.chat.id, 'Not Found')
    else:
        bot.send_message(message.chat.id, start_text)



bot.infinity_polling()