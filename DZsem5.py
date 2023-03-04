# Задача 26:  Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.

# *Пример:*
# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8 

def power(base, exp):
    if (exp == 1):
        return (base)
    if (exp != 1):
        return (base * power(base, exp - 1))
base = int(input("Введите число: "))
exp = int(input("Введите его степень: "))
print("Результат возведения в степень равен:", power(base, exp))

# Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.

# *Пример:*
# 2 2
#     4 

def recsum(a, b):
    return recsum(a+1, b-1) if b > 0 else recsum(a-1, b+1) if b < 0 else a
 
 
a = int(input("A = "))
b = int(input("B = "))
print(f"A + B = {recsum(a, b)}")

# Задача 1: Строка представляет собой арифметическое выражение из однозначных чисел и знаков + и -. Вычислите результат.
# Пример
# Ввод:
# 8-5+2-1
# Вывод:
# 4

expr = input()
res = int(expr[0])
for i in range(1, len(expr), 2):
    if expr[i] == '+':
        res += int(expr[i + 1])
    elif expr[i] == '-':
        res -= int(expr[i + 1])
print(res)

# Задача 2: Словом в данной задаче считается последовательность букв, ограниченная пробелами или началом или концом строки. Выведите все слова из строки в столбик. НЕЛЬЗЯ ПОЛЬЗОВАТЬСЯ МЕТОДАМИ СТРОК (split)
# Формат ввода: вводится строка. Формат вывода: выведите слова из строки по одному.

# Пример 1
# Ввод
# Hello, world!
# Вывод
# Hello,
# world!

# Пример 2
# Ввод
# My heart in the Highland
# Вывод
# My
# heart
# in
# the
# Highland

single_line = input()
words_in_lines = '\n'.join(single_line.split())
words_in_lines = single_line.replace(' ', '\n')
print (words_in_lines)