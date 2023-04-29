# Задача 26:  Напишите программу, которая на вход принимает два числа A и B, 
# и возводит число А в целую степень B с помощью рекурсии.

# *Пример:*

# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8 

number_1 = int(input("Введите целое число "))
degree_1 = int(input("Введите целую степень "))

def exponent(a, b):
    if b == 1:
        return a
    elif b == 0:
        return 1
    return a * exponent(a, b - 1)

print(exponent(number_1, degree_1))