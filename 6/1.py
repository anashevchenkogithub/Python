# Задача 30:  Заполните массив элементами арифметической прогрессии. 
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. 
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

number_1 = int(input("Введите первое число "))
len_p = int(input("Введите количество элементов в последовательности "))
step_p = int(input("Введите шаг прогрессии "))

progression = []

for i in range (0, len_p):
    progression.append(number_1 + i * step_p)

print(progression)