# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

# number = int(input('Введите число :'))


# def Factorial(n):
#     listA = []
#     count = 1
#     for i in range(1, n + 1):
#         listA.append(i * count)
#         count *= i
#     return listA


# print(Factorial(number))

import math
list = [math.factorial(i+1) for i in range(int(input('Введите число :')))]
print(list)