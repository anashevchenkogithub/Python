# Задача 8: Требуется определить, можно ли от шоколадки размером 
# n × m долек отломить k долек, если разрешается сделать один разлом 
# по прямой между дольками (то есть разломить шоколадку на два прямоугольника).

# *Пример:*

# 3 2 4 -> yes
# 3 2 1 -> no

n = int(input("Введите количество долек по длине шоколадки "))
m = int(input("Введите количество долек по  ширине шоколадки "))
k = int(input("Введите сколько долек хотите отломить "))

if k < m * n:
    if (k % m == 0 or k % n == 0):
        print(f"Можно отломить {k} долек одним разломом")
    else: 
        print(f"Нельзя отломить {k} долек одним разломом")
elif k == m * n:
    print(f"Не надо ломать шоколадку. Возьмите ее целиком!")
else:
    print(f"В шоколадке меньше долек, чем Вы хотите отломить")
        