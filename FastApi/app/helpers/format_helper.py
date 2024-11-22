from datetime import date, datetime, time

import pytz
from dateutil import parser

def convert_to_local_time(utc_time: datetime, timezone: str = 'America/Bogota') -> datetime:
    """
    Converts a UTC datetime to a datetime object in the specified local timezone.

    :param utc_time: The datetime object in UTC to be converted.
    :param timezone: The target timezone (default is 'America/Bogota').
    :return: A datetime object in the specified timezone.
    """
    local_timezone = pytz.timezone(timezone)
    local_time = utc_time.astimezone(local_timezone)
    return local_time


def datetime_to_str(_datetime: date) -> str:
    return _datetime.isoformat()


def str_to_datetime(string: str) -> datetime:
    return parser.parse(string)


def date_to_str(_date: datetime) -> str:
    return _date.isoformat()


def str_to_date(string: str) -> date:
    return parser.parse(string).date()


def time_to_str(_time: time) -> str:
    return _time.isoformat()


def str_to_time(string: str) -> time:
    return parser.parse(string).time()
