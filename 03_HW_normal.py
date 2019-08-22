# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1

def fibonacci(n, m):
    list_ = [1, 1]
    for i in range(2, m):
        list_.append(int(list_[i - 1]) + int(list_[i - 2]))
    print(list_[n:m])

fibonacci(int(input('Введите номер начального элемента: ')), int(input('Введите номер последнего элемента: ')))

# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()

import math


def sort_to_max(origin_list):
    sort_list = list()
    while len(origin_list) > 0:
        min = math.inf
        for i in origin_list:
            if i < min:
                min = i
        origin_list.remove(min)
        sort_list.append(min)
    print(sort_list)


sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0])


# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.
list_for_3 = [2, 10, -12, 2.5, 20, -11, 4, 4, 0]


def filter_(func_, list_=list()):
    new_list = []
    for i in list_:
        if func_(int(i)):
            new_list.append(i)
    return new_list


def func_(param):
    if param > 0:
        return True
    else:
        return False


print(filter_(func_, list_for_3))


# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.


import random


A1 = (random.randint(1, 9), random.randint(1, 9))
A2 = (random.randint(1, 9), random.randint(1, 9))
A3 = (random.randint(1, 9), random.randint(1, 9))
A4 = (random.randint(1, 9), random.randint(1, 9))
acbd_ = 0
abcd_ = 0

if math.sqrt(((A1[0] - A2[0]) ** 2) + (A1[1] - A2[1]) ** 2) == math.sqrt(((A3[0] - A4[0]) ** 2) + (A3[1] - A4[1]) ** 2):
    abcd_ = 1
if math.sqrt(((A1[0] - A3[0]) ** 2) + (A1[1] - A3[1]) ** 2) == math.sqrt(((A2[0] - A4[0]) ** 2) + (A2[1] - A4[1]) ** 2):
    acbd_ = 1
if abcd_ == 1 and acbd_ == 1:
    print(f'Вершины являются вершинами параллелограмма: {A1}, {A2}, {A3}, {A4}')
    print(math.sqrt(((A1[0] - A2[0]) ** 2) + (A1[1] - A2[1]) ** 2))
    print(math.sqrt(((A3[0] - A4[0]) ** 2) + (A3[1] - A4[1]) ** 2))
    print (math.sqrt(((A1[0] - A3[0]) ** 2) + (A1[1] - A3[1]) ** 2))
    print (math.sqrt(((A2[0] - A4[0]) ** 2) + (A2[1] - A4[1]) ** 2))
else:
    print(f'Вершины не являются вершинами параллелограмма: {A1}, {A2}, {A3}, {A4}')
    print(math.sqrt(((A1[0] - A2[0]) ** 2) + (A1[1] - A2[1]) ** 2))
    print(math.sqrt(((A3[0] - A4[0]) ** 2) + (A3[1] - A4[1]) ** 2))
    print (math.sqrt(((A1[0] - A3[0]) ** 2) + (A1[1] - A3[1]) ** 2))
    print (math.sqrt(((A2[0] - A4[0]) ** 2) + (A2[1] - A4[1]) ** 2))