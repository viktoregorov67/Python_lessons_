#Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.

def my_round(number, ndigits):
    number *= (10 ** ndigits)
    number_1 = number % 1

    if number_1 >= 0.5:
        number += (1 - number_1)
    else:
        number -= number_1

    number /= (10 ** ndigits)
    return number


print(my_round(2.1234567, 5))
print(my_round(2.1999967, 5))
print(my_round(2.9999967, 5))


# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить

def lucky_ticket(ticket_number):
    my_list = list(map(int, str(ticket_number)))
    if len(my_list) % 2 == 0:
        len_my_list = len(my_list) // 2
    else:
        len_my_list = (len(my_list) // 2) + 1
    if sum(my_list[0:len(my_list) // 2]) == sum(my_list[len_my_list:len(my_list)]):
        fg = "билет счастливый"
    else: fg = "билет несчастливый"
    return fg


print(lucky_ticket(123006))
print(lucky_ticket(12341321))
print(lucky_ticket(436751))