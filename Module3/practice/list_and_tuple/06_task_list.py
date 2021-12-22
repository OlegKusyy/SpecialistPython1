# Даны два целых числа.
# Вывести список всех чисел кратных трем в диапазоне между заданными числами.

first_number = int(input())     # Первое число
second_number = int(input())    # Второе число

# TODO: your code here
# numbers = first_number, second_number
# summa = 0
# # for number in numbers:
#     if number % 3 == 0:
#         summa += number
# print(summa)
i = first_number
summa = 0
while i <= second_number:
    if i % 3 == 0:
        summa += i
    i += 1
print(summa)
