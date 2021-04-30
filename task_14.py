"""
Отсортируйте список из задачи 6 по: товару, по сумме в строке (количество*цену).
Используйте для сортировки лямда функцию.
"""

from task_6 import order

print(sorted(order, key=lambda x: x[0]))
print(sorted(order, key=lambda x: x[1] * x[2]))
