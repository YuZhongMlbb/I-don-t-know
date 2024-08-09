# 1)
# num = int(input('Введите число: '))
# flag = True
# while len(str(num)) != 1:
#     first = num % 10
#     last = num // 10 % 10
#     if first >= last:
#         flag = False
#         break
#     num = num // 10
# if flag:
#     print('Yes')
# else:
#     print('No')

# 2)
# sequence_0 = (14,10,35,45,'60',70,90,0,105,150,10.0,45.0,'70',0)
# sequence_1 = (14,10,35,45,'60',70,90,0,105,150,'70')
# sequence_2 = (14,10,35,45,'60',70,90,0,105,150,10.0,45.0,'70',0.0)
# sequence_3 = (14,10,35,45,'60',70,90,0,105,150,10.0,45.0,'70')
# flag = True
# lst = input('Введите список: ')
# for i in range(0, len(lst) - 1):
#     if lst.count(lst[i]) >= 2:
#         flag = False
#         break
# if flag:
#     print('Последовательность уникальна.')
# else:
#     print('Последовательность не уникальна.')

# # 3
# numbers = [1,0,-2,4,3,6,6,3,5,8,4,2]
# counter = 0
# for i, v in enumerate(numbers):
#     if i == len(numbers) - 1:
#         break
#     if v < numbers[i + 1]:
#         print(numbers[i + 1])

# # 4
# numbers = [2,4,7,1,8.4,-3.3,7.1,-2,4,-1,7,-43,8,-3,6,9]
# parity = 0
# oddness = 0
# for i in numbers:
#     if i % 2 == 0:
#         parity += 1
#     else:
#         oddness += 1
# print(f'Чётных - {parity}, нечётных - {oddness}.')

# # 5
# for i in range(2, 601, 2):
#     print(i, end=', ')

# # 6
# a = 1
# summ = 0
# while a <= 50:
#     summ += a
#     a += 1
# print(summ / 50)

# # 7
# a = int(input('Введите случайное число: '))
# flag = True
# while a != 7:
#     flag = False
#     b = int(input('Не угадали. Введите снова: '))
#     if b == 7:
#         break
# if flag:
#     print(f'Вы угадали, это число {a}')
# if not flag:
#     print(f'Вы угадали, это число {b}')

# # 8
# for i in range(100, 1000):
#     i = str(i)
#     if int(i[0]) + int(i[1]) + int(i[2]) == 5:
#         print(i, end=', ')

# # 9
# for i in range(1, 21):
#     if i == 13:
#         continue
#     print(i, end=', ')

# # 10
# summ = 0
# for i in range(1, 101):
#     if i % 3 == 0:
#         continue
#     summ += i
# print(summ)

# # 11
# a = 100
# while a >= 1:
#     print(a, end=', ')
#     a -= 1

# # 12
# a = input('Введите строку: ')
# if a == a[::-1]:
#     print('Палиндром')
# else:
#     print('Не палиндром')

# # 13
# string = "4729461084"
# summ = 0
# for i in string:
#     summ += int(i)
# print(summ)

# # 14
# while True:
#     a = int(input('Введите число: '))
#     b = int(input('Введите число: '))
#     action = input('+, -, *, /...? ')
#     if action == '+':
#         print(a + b)
#     elif action == '-':
#         print(a - b)
#     elif action == '*':
#         print(a * b)
#     elif action == '/':
#         print(a / b)
#     else:
#         print('Ошибка.')
#     close = input('Вы хотите продолжить? Да/Нет: ').lower()
#     if close == 'нет':
#         print('Завершение работы...')
#         break

# # 15
# a = input('Введите число: ')
# while not a.isdigit():
#     b = input('Не число. Повторите снова: ')
#     if b.isdigit():
#         break

# # 16
# a = input('Введите число: ')
# b = input('Введите число: ')
# flag = True
# while (not a.isdigit()) or (not b.isdigit() or int(b) == 0):
#     flag = False
#     print('Не числа/число!')
#     c = input('Введите число: ')
#     d = input('Введите число: ')
#     if (and c.isdigit()) and (int(d) > 0 and d.isdigit()):
#         break
# if flag:
#     print(int(a)/int(b))
# else:
#     print(int(c)/int(d))

# # 17
# a = [1, '2', 3, 'a', 'i']
# for i in a:
#     if type(i) == int:
#         continue
#     elif type(i) == str and i.isdigit():
#         continue
#     else:
#         print(f'Ошибка - {i}')

# # 18
# a = input('Введите число: ')
# while not a.isdigit():
#     print('Не число')
#     b = input('Введите число: ')
#     if b.isdigit():
#         break

