# Домашнее задание по теме "Декораторы"
# Задание:
# Напишите 2 функции:
# Функция которая складывает 3 числа (sum_three)
# Функция декоратор (is_prime), которая распечатывает "Простое",
# если результат 1ой функции будет простым числом и "Составное" в противном случае.
# Пример:
# result = sum_three(2, 3, 6)
# print(result)
#
# Результат консоли:
# Простое
# 11
#
# Примечание:
# Не забудьте написать внутреннюю функцию wrapper в is_prime
# Функция is_prime должна возвращать wrapper
# @is_prime - декоратор для функции sum_three
def is_prime(func):
    def wrapper(*args):
        x = func(*args)
        k=0
        for i in range(2, x//2+1):
            if (x % i == 0):
                k=k+1
        if x == 0:
            return f'{x} - не относится к простым или составным числам'
        if x == 1:
            return f'{x} - не относится к простым или составным числам'
        if (k<=0):
            return f'Простое\n{x}'
        else:
            return f'Составное\n{x}'
    return wrapper

@is_prime
def sum_three(*args):
    a=sum(args)
    return a

result = sum_three(2, 3, 6)
print(result)

