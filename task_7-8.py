"""
Из задачи 6 постройте два списка идентификаторов товаров так, чтобы в каждом не было
повторений
"""
from task_6 import order
import time


def postroenie_dvuh_spiskov(array):
    array_1 = set()
    array_2 = set()
    for elem in array:
        array_1.add(elem[0])
        array_2.add(elem[0])
    return array_1, array_2


def dorabotka_spiskov(array):
    array_1, array_2 = postroenie_dvuh_spiskov(array)
    print(f'Первый список с идентификаторами - {list(array_1)},\nВторой список с идентификаторами - {list(array_2)}')
    print('___________________________________________________________________________________')
    print('Производится объединение списков...')
    time.sleep(2)
    print('...')
    time.sleep(2)
    print('Перевожу списки в множества')
    time.sleep(2)
    print(f'в виде множества... SETFROZENSET_set_from_list_{array_1}')
    time.sleep(2)
    print('Беру объединения и пересечения... ')
    time.sleep(2)
    print('...')
    print(f'ГОТОВО -------------- {sorted(array_1)}')


if __name__ == '__main__':
    dorabotka_spiskov(order)
