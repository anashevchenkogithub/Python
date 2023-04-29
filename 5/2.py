# Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму 
# двух целых неотрицательных чисел. Из всех арифметических операций 
# допускаются только +1 и -1. Также нельзя использовать циклы.

# *Пример:*

# 2 2
#     4 

n1 = int(input("Введите целое неотрицательное число "))
n2 = int(input("Введите целое неотрицательное число "))

def sum(a, b):
    if b == 0:
        return a
    return 1 + sum(a, b - 1)

print(sum(n1, n2))