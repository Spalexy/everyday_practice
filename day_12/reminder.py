from datetime import datetime, timedelta


def get_remaining_time_(current_time: str, future_time: str) -> str:
    current_time_in_datetime = datetime.strptime(current_time, '%H:%M')
    future_time_in_datetime = datetime.strptime(future_time, '%H:%M')
    if future_time_in_datetime <= current_time_in_datetime:
        future_time_in_datetime += timedelta(days=1)
    time_delta = future_time_in_datetime - current_time_in_datetime

    return ':'.join(str(time_delta).split(':')[:2])


print(get_remaining_time_('12:00', '11:10'))
