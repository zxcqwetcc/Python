# num2 =[[1,11],[4,11 ]]
# min2 = num2[0]
# max2 = num2 [1]
# for i in num2(0):
#     for j in num2(1):
#         if i > max2:
#             max2 = i
#             print("Максимум", min2)
#         elif i < min2:
#             min2 = i      
# print("Минимум",min2 )
  

# for i in range(1, 10):
#     for  j in range(1, 10):
#         print(i, "*", j, "=", i * j)
    
# j = [1, 2, 3, 4, 5, 6]
# j2 = [i for i in j if i <21]
# print(j2)

# num1 = [[0, 23,],[3, 4]]

# min1 = num1[0][0]
# max2 = num1[0][0]

# for i in num1:
#     for j in i:
#         if j > max2:
#             max2 = j 
#         if j < min1:
#             min1 = j
        
# print("Minimum",min1)
# print("Maximum",max2)



# a = [[1, 2, 3,],[4, 5, 6]]
# for i in a:
#     for j in i:
#         print(i)
 
# numm = [[1,5],[3,4]]
# for i in numm:
#     for j in i:
#         print()


# num1 = [
# [1, 2, 3],
# [4, 5, 6],
# [7, 8, 9]
# ]
# print(num1[0])
# print(num1[1])
# print(num1[2])

# num1 = int(input("Введите первое число: "))
# ope = input("Выберите операцию(+, -, *, /: )")
# num2 = int(input("Введите второе число: "))
# ope = input("Выберите операцию(+, -, *, /: )")
# num3 = int(input("Введите третье число: "))
# if ope == '+':
#     res = num1 + num2 + num3
# elif ope == '-':
#     res = num1 - num2 - num3
# elif ope == '*':
#     res = num1 * num2 * num3
# elif ope == '/':
#  res = num1 / num2 / num3       
# print("Результат: ",res)\

# num1 = input("Введите первое число: ")
# if num1.lower() == "стоп":
#     exit()
# num1 = int(num1)
# while True:
#     op = input("Операция (+, -, *, /): ")
#     if op.lower() == "стоп" :
#         break
#     num2 = input("Введите след. число: ")
#     if num2.lower() == "стоп":
#         break
#     num2 = int(num2)
#     if op == '+':
#         num1 += num2
#     elif op == '-':
#         num1 -= num2
#     elif op == '*':
#         num1 *= num2
#     elif op == "/":
#         if num2 == 0:
#             print("Ошибка: деление на 0")
#             break
# print("Результат: ", num1)

# w = int(input("Введите ширину: "))
# h = int(input("Введите высоту: "))

# for i in range(h):
#     for j in range(w):
#         if  i == 0 or i == h -1 or j == 0 or j == w -1:
#             print("+", end=" ")
#         else:
#             print(" ", end=" ")
#     print()

# snumber = int(input("1 Игрок напиши чилсо от 1 до 101: "))
# print("\n * 50")
# try_count = 0
# user_number = 0
# while user_number != snumber:
#     try_count += 1
#     user_number = int(input(f"{try_count} -Я попытка"))
#     if user_number > snumber:
#         print("Много")
#     if user_number < snumber:
#         print("Мало")
#     else:
#         print("Ты угадал правильно, я загадал{snumber}, ты угадал за {try_count} попыток")

print("= 1 Раунд =")
snumber1 = int(input("1 игрок загадайте  число от 1 до 101: "))
print("\n * 50")
print("2 игрок угадайте загаданное число: ")
user_number = 0 
trys2 = 0

while user_number != snumber1:
    trys2 += 1 
    user_number = int(input(f"{trys2}-я попытка: "))

    if user_number > snumber1:
        print("Много")
    elif user_number < snumber1:
        print("Мало")
    else:
        print(f"Ты правильно угадал, за {trys2} попыток")

print("= 2 Раунд =")
snumber2 = int(input("2 игрок загадайте число от 1 до 101: "))
print("\n * 50")
print("1 игрок угадайте загаданное число: ")
user_number = 0 
trys1 = 0

while user_number != snumber2:
    trys1 += 1
    user_number = int(input(f"{trys1}-я попытка: "))

    if user_number > snumber2:
        print("Много")
    elif user_number < snumber2:
        print("Мало")
    else:
        print(f"Ты правильно угадал, за {trys1} попыток:")

print("\nРезультаты:")
print(f"Игрок 1 угадал за {trys1} попыток.")
print(f"Игрок 2 угадал за {trys2} попыток.")

if trys1 < trys2:
    print("Победил 1 игрок")
elif trys1 > trys2:
    print("Победил 2 игрок")
else:
    print("Ничья")
