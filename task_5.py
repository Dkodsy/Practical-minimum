"""
Пользователь вводит две даты в формате ДД.ММ.ГГГГ ЧЧ:ММ. Пользователь вводит
третью дату в формате ДД.ММ.ГГГГ ЧЧ:ММ. Определить, лежит ли дата внутри
временного интервала, образованного первыми двумя датами.
"""
from task_3 import date_check


def date_occurrence(checked_date, checked_date_2, checked_date_3):
    if checked_date <= checked_date_3 <= checked_date_2:
        print('Входит')
    elif checked_date_2 <= checked_date_3 <= checked_date:
        print('Входит')
    else:
        print('Не входит')


if __name__ == "__main__":
    date_1 = date_check(input('Введите первую дату в формате ДД.ММ.ГГГГ ЧЧ:ММ: '))
    date_2 = date_check(input('Введите вторую дату в формате ДД.ММ.ГГГГ ЧЧ:ММ: '))
    date_3 = date_check(input('Введите третью дату, которую нужно определить, в формате ДД.ММ.ГГГГ ЧЧ:ММ: '))
    date_occurrence(date_1, date_2, date_3)
"""
12.02.2021 15:17
12.05.2021 17:01
12.04.2021 20:17
13.12.2021 15:17
"""
