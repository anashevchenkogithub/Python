# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. 
# Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000), 
# а Катя должна их отгадать. Для этого Петя делает две подсказки. Он называет сумму этих 
# чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.


# Математическое решение через формулу квадратного уравнения

# s = int(input("Введите сумму чисел "))
# p = int(input("Введите произведение чисел "))

# d = s * s - 4 * p # дискриминант квадратного уравнения
# x1 = (s - d ** 0.5) / 2
# x2 = (s + d ** 0.5) / 2

# if d < 0:
#     print("Нет решения")
# elif d == 0:
#     print(f"Искомые числа {s / 2} и {s - s / 2}")
# elif x1 < 0:
#     if x2 % 1 == 0:
#         print(f"Искомые числа {int(x2)} и {int(s - x2)}")
# else:
#     if x1 % 1 == 0:
#         print(f"Искомые числа {int(x1)} и {int(s - x1)}")
#     if x2 % 1 == 0:
#         print(f"Искомые числа {int(x2)} и {int(s - x2)}")

# Решение через перебор

s = int(input("Введите сумму чисел "))
p = int(input("Введите произведение чисел "))

for i in range(s):
    for j in range(s):
        if s == i + j and p == i * j:
            print(f"Искомые числа {i} и {j}")