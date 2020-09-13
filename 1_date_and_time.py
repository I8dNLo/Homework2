"""
Домашнее задание №2

Дата и время

1. Напечатайте в консоль даты: вчера, сегодня, 30 дней назад
2. Превратите строку "01/01/20 12:10:03.234567" в объект datetime

"""
from datetime import datetime, timedelta


def print_days():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    date_today = datetime.now()
    print(f"Текущая дата: {date_today.strftime('%d.%m.%Y')}")
    date_yesterday = date_today - timedelta(days = 1)
    print(f"Вчера было: {date_yesterday.strftime('%d.%m.%Y')}")
    date_month_ago = date_today - timedelta(days = 30)
    print(f"30 дней назад было: {date_month_ago.strftime('%d.%m.%Y')}")




def str_2_datetime(date_string):
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    date_dt = datetime.strptime(date_string, '%m/%d/%y %H:%M:%S.%f')
    return date_dt


if __name__ == "__main__":
    print_days()
    print(str_2_datetime("01/01/20 12:10:03.234567"))
