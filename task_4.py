"""
Пользователь вводит две даты в формате ДД.ММ.ГГГГ ЧЧ:ММ. Вывести разницу между
датами в часах, днях (целых), минутах и секундах.
"""
from task_3 import date_check


def date_diff(checked_date, checked_date_2):

    date_difference = (checked_date_2 - checked_date)
    diff_in_seconds = date_difference.total_seconds()
    diff_in_hour = diff_in_seconds / 60 // 60
    diff_in_days = date_difference.days
    diff_in_minutes = diff_in_seconds / 60
    print(f'Разница в кол-ве часов - {diff_in_hour}\n'
          f'в кол-ве дней - {diff_in_days}\n'
          f'в кол-ве минут - {diff_in_minutes}\n'
          f'в кол-ве секунд - {diff_in_seconds}')

    return diff_in_hour, diff_in_days, diff_in_minutes, diff_in_seconds


if __name__ == "__main__":
    date_1 = date_check(input('Введите первую дату в формате ДД.ММ.ГГГГ ЧЧ:ММ:'))
    date_2 = date_check(input('Введите вторую дату в формате ДД.ММ.ГГГГ ЧЧ:ММ:'))
    date_diff(date_1, date_2)

"""
12.02.2021 15:17
12.12.2021 17:01
"""
