import datetime

from config import USER_NAME


def time_of_day_greeting():
    now_hour = datetime.datetime.now().hour

    if 0 <= now_hour < 5:
        greeting = 'Доброй ночи, {}!'.format(USER_NAME)
    elif 5 <= now_hour < 10:
        greeting = 'Доброе утро, {}!'.format(USER_NAME)
    elif 10 <= now_hour < 17:
        greeting = 'Добрый день, {}!'.format(USER_NAME)
    else:
        greeting = 'Добрый вечер, {}!'.format(USER_NAME)
    return greeting


print(time_of_day_greeting())