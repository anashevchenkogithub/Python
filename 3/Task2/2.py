# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент
# к заданному числу X. Пользователь в первой строке вводит натуральное число N – 
# количество элементов в массиве. В последующих  строках записаны N целых чисел Ai. 
# Последняя строка содержит число X

# *Пример:*

# 5
#     1 2 3 4 5
#     6
#     -> 5

massive_size = int(input("Введите количество целых чисел "))
list_1 = [i + 1 for i in range(massive_size)]
print(list_1)
number_to_find = int(input("Введите число для поиска "))

for i in range(1, len(list_1) + 1):
    if list_1[i - 1] == number_to_find:
        print(number_to_find)
if number_to_find < list_1[0]:
    print(list_1[0])
elif number_to_find > list_1[massive_size - 1]:
    print(list_1[massive_size - 1])
