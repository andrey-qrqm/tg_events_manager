import gs_test
from datetime import datetime, timedelta

today = datetime.now()

blocked_keys = [
    "Отметка времени",
    "Адрес электронной почты",
    "Date",
    "Time",
    "Place",
    "Topic",
    "Tags",
    "Event Name",
    "Organiser"
]


def reply_generator(n):
    filtered_data = gs_test.filter_records(gs_test.all_records, 'Date', today, today + timedelta(days=int(n) - 1))
    data = gs_test.sort_records(filtered_data)
    reply = ""
    message = ""

    for event in data:
        message = "--------------------------------\n"
        message += f'{event["Date"]}: \n'
        message += f'{event["Event Name"]} by {event["Organiser"]} at {event["Time"]}: \n'
        message += f'Place - {event["Place"]}: \n'
        message += f'Topic - {event["Topic"]}: \n'
        message += f'Tags - {event["Tags"]}: \n'

        for key in event:
            if key not in blocked_keys:
                message += f'{key} - {event[key]}\n'
        reply += message + '\n'

    return reply


reply = reply_generator(3)
print(reply)