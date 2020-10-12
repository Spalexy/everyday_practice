from requests import get as r_get

from config import USER_NAME, TIME_API_LINK


def get_current_hour_from_worldtimeapi():
    date_time = r_get(TIME_API_LINK).json().get('datetime')
    return int(date_time[11:13])


def get_greeting_line_by_current_hour(now_hour):
    if 0 <= now_hour < 5:
        greeting = 'Доброй ночи, {}!'.format(USER_NAME)
    elif 5 <= now_hour < 10:
        greeting = 'Доброе утро, {}!'.format(USER_NAME)
    elif 10 <= now_hour < 17:
        greeting = 'Добрый день, {}!'.format(USER_NAME)
    else:
        greeting = 'Добрый вечер, {}!'.format(USER_NAME)
    return greeting


print(get_greeting_line_by_current_hour(get_current_hour_from_worldtimeapi()))
