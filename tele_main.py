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
    """
    if message.text.startswith("event"): 
        try:
            days = int(message.text[6:])
            EventsReply = reply_generator(days)
        except TypeError:
            EventsReply = "This command is not correct, type help to see correct commands"
        if EventsReply != "":
            bot.send_message(message.from_user.id, EventsReply)
        else:
            EventsReply = "Currently there are no events at this date"
            bot.send_message(message.from_user.id, EventsReply)
       """
    if message.text == "event":
        EventsReply = reply_generator(1)
        if EventsReply != "":
            bot.send_message(message.from_user.id, EventsReply)
        else:
            EventsReply = "Currently there are no events at this date"
            bot.send_message(message.from_user.id, EventsReply)
    elif message.text == "event 3":
        EventsReply = reply_generator(3)
        if EventsReply != "":
            bot.send_message(message.from_user.id, EventsReply)
        else:
            EventsReply = "Currently there are no events at this date"
            bot.send_message(message.from_user.id, EventsReply)
    elif message.text == "event 7":
        EventsReply = reply_generator(7)
        if EventsReply != "":
            bot.send_message(message.from_user.id, EventsReply)
        else:
            EventsReply = "Currently there are no events at this date"
            bot.send_message(message.from_user.id, EventsReply)
    else:
        bot.send_message(message.from_user.id, """
        This command does not exist.
        Available commands:
        event - Events for today
        event 3 - Events for 3 days
        event 7 - Events for a week
        """)


if __name__ == '__main__':
    bot.polling(none_stop=True, interval=5)

