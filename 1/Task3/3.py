# Задача 6: Вы пользуетесь общественным транспортом? 
# Вероятно, вы расплачивались за проезд и получали билет с номером. 
# Счастливым билетом называют такой билет с шестизначным номером, где сумма 
# первых трех цифр равна сумме последних трех. 
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. 
# Вам требуется написать программу, которая проверяет счастливость билета.

# *Пример:*

# 385916 -> yes
# 123456 -> no

a = int(input("Введите 6-ти значный номер билета "))
if len(str(a)) != 6:
    print("Этот номер не подходит")
else: 
    a = str(a)
    if int(a[0]) + int(a[1]) + int(a[2]) == int(a[-1]) + int(a[-2]) + int(a[-3]):
        print(f"Билет номер {a} счастливый")
    else: 
        print(f"Билет номер {a} несчастливый")