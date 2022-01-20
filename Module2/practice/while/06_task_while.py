# Два натуральных числа называются дружественными, если каждое из них равно сумме всех натуральных делителей другого
# (само число при этом не рассматривается в качестве собственного делителя).
# Необходимо найти все пары натуральных дружественных чисел (не равных друг другу),
# оба числа в которых меньше вводимого с клавиатуры числа N.
# Дано натуральное число n, требуется проверить его на простоту.

# Формат входных данных: Вводится одно целое число N (1≤N≤10000).
# Формат выходных данных: Требуется вывести все пары дружественных чисел,
# удовлетворяющие условию задачи. Пары можно выводить в любом порядке.

# Пример:
# Входные данные
# 300
# Выходные данные
#
# 220 284
# 284 220

# TODO: your code here

N = 10000
number1 = 1
opti_factor = 2

while number1 <= N:
    divider_number1 = 1
    sum_divider_number1 = 0
    while divider_number1 * opti_factor <= number1:
        if number1 % divider_number1 == 0:
            sum_divider_number1 += divider_number1
        divider_number1 += 1
    # if sum_divider_number1 == 1:
    #     print("Простое число -", number1)
    # print(number1, "Сумма делителей", sum_divider_number1)
    if 1 < sum_divider_number1 <= N:
        # print(number1, "Сумма делителей", sum_divider_number1)
        number2 = sum_divider_number1
        divider_number2 = 1
        sum_divider_number2 = 0
        while divider_number2 * opti_factor <= number2:
            if number2 % divider_number2 == 0:
                sum_divider_number2 += divider_number2
            divider_number2 += 1
        # print(number2, sum_divider_number2)
        if number1 == sum_divider_number2 and number1 != number2:
            print("Дружественные числа -", number1, number2)
    number1 += 1
