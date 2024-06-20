import telebot

import re
from sys import argv
from sort_Test import reply_generator

# Taking token as a start parameter
script, token = argv
bot = telebot.TeleBot(token)


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    message.text = message.text.lower()

    if message.text.startswith("event"): 
        try:
            days = int(message.text[6:])
            EventsReply = reply_generator(days)
        except ValueError:
            EventsReply = reply_generator(1)
        if EventsReply != "":
            bot.send_message(message.from_user.id, EventsReply)
        else:
            EventsReply = "Currently there are no events at this date"
            bot.send_message(message.from_user.id, EventsReply)
    elif message.text.startswith('help'):
        EventsReply = """Command:
event DAYS - see events in the next days (put your number instead of DAYS)"""
        bot.send_message(message.from_user.id, EventsReply)
    else:
        EventsReply = "I don't know this command, please type help to see list of commands"
        bot.send_message(message.from_user.id, EventsReply)

if __name__ == '__main__':
    bot.polling(none_stop=True, interval=5)

