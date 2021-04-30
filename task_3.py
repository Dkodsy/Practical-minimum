"""
Пользователь вводит дату и время в формате ДД.ММ.ГГГГ ЧЧ:ММ. Обрежьте секунды.
Замените час на 10.
"""
from datetime import datetime
import time


def date_check(input_str):
    try:
        return datetime.strptime(input_str, '%d.%m.%Y %H:%M')
    except:
        print('Неверная дата или время!')
        return date_check(input('Попробуйте еще раз:'))


def obrezanie_and_zamena(checked_date):
    print(f'Вы ввели {datetime.strftime(checked_date, "%d.%m.%Y %H:%M:%S")}')
    print('Проводится обрезание секунд...\n\n')
    time.sleep(2)
    print('......\n\n')
    time.sleep(2)
    print('Замена часа на "10"...\n\n')
    time.sleep(3)
    print('......\n\n')
    time.sleep(2)
    print(f'Ваша дата и время! - {datetime.strftime(checked_date, "%d.%m.%Y %H:%M")}')


if __name__ == "__main__":
    date = date_check(input('Введите дату и время!: '))
    obrezanie_and_zamena(date)

"""
12.02.2021 15:17
12.05.2021 17:01
12.04.2021 20:17
13.12.2021 15:17
"""