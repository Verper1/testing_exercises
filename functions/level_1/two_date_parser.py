import datetime


def compose_datetime_from(date_str: str, time_str: str) -> datetime.datetime:
    """
    Отдаёт дату и время, которое либо сейчас, либо будут завтра по введенному "tomorrow"/

    Пример:
    compose_datetime_from("tomorrow", "09:15") -> datetime.datetime(2026, 3, 4, 9, 15)
    compose_datetime_from("today", "14:30") -> datetime.datetime(2026, 3, 3, 14, 30)
    """
    date = datetime.date.today()
    if date_str == "tomorrow":
        date += datetime.timedelta(days=1)

    hour_str, minute_str = time_str.strip().split(":")
    return datetime.datetime(
        date.year,
        date.month,
        date.day,
        int(hour_str),
        int(minute_str),
    )
