# Задайте рандомно список из чисел размером N, где N число с клавиатуры.
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

# import random

# n = int(input("Введите размер списка: "))
# ListA = []

# def FillArray(List):
#     for i in range(n):
#         List.append(random.randint(-10, 10))
#     return List

# FillArray(ListA)

# summ = 0
# for i in range(1, len(ListA), 2):
#     summ += ListA[i]

# print(F"{ListA}  сумма элементов на нечётных позициях: {summ}")

import random

listA = dict(enumerate(random.randrange(-10, 10, 1) for i in range(int(input("Введите размер списка: ")))))

print(listA,'\n','Cумма элементов на нечётных позициях = ',(sum([(listA[key]) for key in sorted(listA)[1::2]])))