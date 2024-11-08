from datetime import date, datetime, time

import pytz
from dateutil import parser


def get_colombian_timezone():
    return pytz.timezone("America/Bogota")


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
