"""
Пользователь вводит дату в формате ДД.ММ.ГГГГ. Вывести первый день месяца,
последний день месяца, сам месяц.
"""
import datetime
import calendar

months = ['январь', 'февраль', 'март', 'апрель', 'май', 'июнь',
          'июль', 'август', 'сентябрь', 'октябрь', 'ноябрь', 'декабрь']

try:
    date = datetime.datetime.strptime(input('Введите дату: '), '%d.%m.%Y')
    last_day = calendar.monthrange(year=date.year, month=date.month)[-1]
    print(f'Первое число - 1, последнее число - {last_day}, месяц - {months[date.month - 1]}')
except:
    print('Вы ввели неверную дату :(')
