"""
9. Создайте класс. Пусть в нем будут поля Фамилия, Имя, Год рождения.
10. Создайте метод, который выводит ФИО.
11. Создайте метод, который вычисляет возраст в годах.
12. Создайте класс - наследник вашего первого класса. Перекройте в нём метод,
вычисляющий возраст в годах на метод, который вычисляет возраст в днях.
13. Создайте декоратор для метода, который выводит ФИО. Пусть новый метод выводит
ФИО, заключенное в теги <strong>.
"""
from datetime import datetime


class FullName:
    def __init__(self, surname: str, name: str, year_of_birth: int):
        self.surname = surname
        self.name = name
        self.year_of_birth = year_of_birth

    def printing_fullname(self):
        print(self.surname, self.name)

    def calculated_age(self):
        age = datetime.now().year - self.year_of_birth
        return age


class Daughter(FullName):
    def calculated_age(self):
        age = datetime.now().year - self.year_of_birth
        age_in_days = age * 365
        return age_in_days


def decorator(func):
    def wrapper(*args, **kwargs):
        print("<strong>")
        func(*args, **kwargs)
        print("</strong>")
    return wrapper


if __name__ == '__main__':
    name_sur = FullName('Ivan', 'Ivanov', 1998)
    name_sur.printing_fullname()
    print(f'кол-во лет - {name_sur.calculated_age()}\n')

    dec_printing = decorator(name_sur.printing_fullname)
    dec_printing()


