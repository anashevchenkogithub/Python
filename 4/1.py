# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, 
# которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества. 
# m — кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.

size_1 = int(input("Введите кол-во чисел в первом множестве "))
size_2 = int(input("Введите кол-во чисел вo втором множестве "))

list_1 = []
for i in range(0, size_1):
    list_1.append(int(input("Введите число ")))
print(list_1)

list_uniq_1 = set(list_1)   

list_2 = []
for i in range(0, size_2):
    list_2.append(int(input("Введите число ")))
print(list_2)

list_uniq_2 = set(list_2) 
   
final_uniq_list = list_uniq_2.union(list_uniq_1)
print(final_uniq_list)