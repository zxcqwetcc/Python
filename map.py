# with open('27 - a.txt') as f:
#     n = int(f.readline())
#     for i in range(n):
#         a, b = ma
#         (int, f.readline().split())
#         print(a * b)


# def f(a, b):
#     return(a * b)
# a = map(lambda x: x + 15, (4, 5, 6))
# print(list(a))


# def f(a):
#      if a % 2 != 0 :
#          return a
# a = filter(f, (1, 2, -3, 4, 5, 6, 7,))
# print(list(a))


# a = filter(lambda x: (x % 2 == 0),(1, 2, 3 , 4, 5, 6)) 
# print(list(a))


# from functools import reduce
# print(reduce(lambda a, b: a * b, (100, 5, 1, 100)))

# a = [1, 2, 3, 4, 5]
# b = 'Sigma'
# result = zip(a, b)
# print(list(result))


# from functools import reduce

# a = [76, 37985, 4, 5, 6, 789, ]
# print(reduce(max, a))

# lst = [12, 33,42342, 543,]
# lst = list(map(int,lst))
# maximum = lst[0]
# for i in range(1,len(lst)):
#     if lst[i] > maximum:
#        maximum = lst[i]

# print(maximum)

# num2 =[[3,11],[2,11 ]]
# min2 = num2[0]
# max2 = num2 [1]
# for i in num2:
#     if i > max2:
#         max2 = i
#         print("Максимум", max2)
#     elif i < min2:
#         min2 = i      
# print("Минимум",min2 )



# num1 = [[1, 2], [3, 4]]

# min1 = num1[0][0]
# max2 = num1[0][0]

# for k in num1:
#     for e in k:num1 = float(input("Введите первое число: "))
# num2 = float(input("Введите второе число: "))
# num3 = float(input("Введите третье число: "))
# operation = input("Введите операцию (+, -, *, /): ")

# if operation == '+':
#     result = num1 + num2 + num3
# elif operation == '-':
#     result = num1 - num2 - num3
# elif operation == '*':
#     result = num1 * num2 * num3
# elif operation == '/':
#     if num2 != 0 and num3 != 0:
#         result = num1 / num2 / num3
#     else:
#         print("Ошибка: деление на ноль")
#         result = None
# else:
#     print("Неверная операция")
#     result = None

# if result is not None:
#     print("Результат:", result)
# #         if e < min1:
#             min1 = e
#         if e > max2:
#             max2 = e

# print("Minimum", min1)
# print("Maximum", max2)

# Раунд 1: Игрок 1 загадывает, Игрок 2 угадывает
print("=== Раунд 1 ===")
secret_number_1 = int(input("Игрок 1, загадай число от 1 до 100: "))
print("\n" * 50)  # Скрываем число

print("Игрок 2, отгадай число от 1 до 100")

user_number = 0
tries_2 = 0

while user_number != secret_number_1:
    tries_2 += 1
    user_number = int(input(f"{tries_2}-я попытка: "))
    
    if user_number > secret_number_1:
        print("Много")
    elif user_number < secret_number_1:
        print("Мало")
    else:
        print(f"Правильно! Ты угадал за {tries_2} попыток.")

# Раунд 2: Игрок 2 загадывает, Игрок 1 угадывает
print("\n=== Раунд 2 ===")
secret_number_2 = int(input("Игрок 2, загадай число от 1 до 100: "))
print("\n" * 50)  # Скрываем число

print("Игрок 1, отгадай число от 1 до 100")

user_number = 0
tries_1 = 0

while user_number != secret_number_2:
    tries_1 += 1
    user_number = int(input(f"{tries_1}-я попытка: "))
    
    if user_number > secret_number_2:
        print("Много")
    elif user_number < secret_number_2:
        print("Мало")
    else:
        print(f"Правильно! Ты угадал за {tries_1} попыток.")

# Сравнение результатов
print("\n=== Результаты ===")
print(f"Игрок 1 угадал за {tries_1} попыток.")
print(f"Игрок 2 угадал за {tries_2} попыток.")

if tries_1 < tries_2:
    print("Победил Игрок 1!")
elif tries_2 < tries_1:
    print("Победил Игрок 2!")
else:
    print("Ничья!")
