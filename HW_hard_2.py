# Задание-1: уравнение прямой вида y = kx + b задано в виде строки.
# Определить координату y точки с заданной координатой x.
print('Задание 1')
equation = 'y = -12x + 11111140.2121'
x = 2.5
# вычислите и выведите y
split_result = equation.split()
arg_with_x = float(split_result[2].replace('x', '')) * float(x)
y = arg_with_x + float(split_result[4])
print('y = ', y)

# Задание-2: Дата задана в виде строки формата 'dd.mm.yyyy'.
# Проверить, корректно ли введена дата.
# Условия корректности:
# 1. День должен приводиться к целому числу в диапазоне от 1 до 30(31)
#  (в зависимости от месяца, февраль не учитываем)
# 2. Месяц должен приводиться к целому числу в диапазоне от 1 до 12
# 3. Год должен приводиться к целому положительному числу в диапазоне от 1 до 9999
# 4. Длина исходной строки для частей должна быть в соответствии с форматом
#  (т.е. 2 символа для дня, 2 - для месяца, 4 - для года)

# Пример корректной даты
#date = '01.11.1985'

# Примеры некорректных дат
#date = '01.22.1001'
#date = '1.12.1001'
#date = '-2.10.3001'

print('Задание 2')
dateInput = input('Введите дату формате dd.mm.yyyy:\n').split('.')

day = int(dateInput[0])
month = int(dateInput[1])
year = int(dateInput[2])
long_month = [1, 3, 5, 7, 8, 10, 12]

if len(dateInput[0]) != 2 or len(dateInput[1]) != 2 or len(dateInput[2]) != 4:
    print('Формат даты введен некорректно. Введите дату формате dd.mm.yyyy:\n')
elif day > 31 or day < 1:
    print('Формат даты введен некорректно. Введите день в диапазоне от 1 до 31\n')
elif month > 12 or month < 1:
    print('Формат даты введен некорректно. Введите месяц в диапазоне от 1 до 12\n')
elif year > 9999 or year < 1:
    print('Формат даты введен некорректно. Введите год в диапазоне от 1 до 9999\n')
elif month not in long_month and day > 30:
    print('Введите корректный день, относительно месяца')
else:
    print('Формат даты введен корректно.', dateInput)

print()

# Задание-3: "Перевёрнутая башня" (Задача олимпиадного уровня)
#
# Вавилонцы решили построить удивительную башню —
# расширяющуюся к верху и содержащую бесконечное число этажей и комнат.
# Она устроена следующим образом — на первом этаже одна комната,
# затем идет два этажа, на каждом из которых по две комнаты,
# затем идёт три этажа, на каждом из которых по три комнаты и так далее:
#         ...
#     12  13  14
#     9   10  11
#     6   7   8
#       4   5
#       2   3
#         1
#
# Эту башню решили оборудовать лифтом --- и вот задача:
# нужно научиться по номеру комнаты определять,
# на каком этаже она находится и какая она по счету слева на этом этаже.
#
# Входные данные: В первой строчке задан номер комнаты N, 1 ≤ N ≤ 2 000 000 000.
#
# Выходные данные:  Два целых числа — номер этажа и порядковый номер слева на этаже.
#
# Пример:
# Вход: 13
# Выход: 6 2
#
# Вход: 11
# Выход: 5 3